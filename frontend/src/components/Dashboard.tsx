import { useState, useEffect } from 'react';
import { Container, Title, Paper, Button, TextInput, Textarea, Grid, Card, Text, Group } from '@mantine/core';
import { useForm } from '@mantine/form';
import { notifications } from '@mantine/notifications';
import { useAuth } from './Auth';
import axios from 'axios';

interface Blog {
  id: number;
  title: string;
  body: string;
  creator: {
    email: string;
    name: string;
  };
}

export function Dashboard() {
  const { token, logout } = useAuth();
  const [blogs, setBlogs] = useState<Blog[]>([]);

  const form = useForm({
    initialValues: {
      title: '',
      body: '',
    },
    validate: {
      title: (value) => (value.length < 3 ? 'Title must be at least 3 characters' : null),
      body: (value) => (value.length < 10 ? 'Body must be at least 10 characters' : null),
    },
  });

  const fetchBlogs = async () => {
    try {
      const response = await axios.get('http://localhost:8000/blog', {
        headers: { Authorization: `Bearer ${token}` },
      });
      setBlogs(response.data);
    } catch (error) {
      notifications.show({
        title: 'Error',
        message: 'Failed to fetch blogs',
        color: 'red',
      });
    }
  };

  useEffect(() => {
    fetchBlogs();
  }, [token]);

  const handleCreateBlog = async (values: typeof form.values) => {
    try {
      await axios.post('http://localhost:8000/blog', values, {
        headers: { Authorization: `Bearer ${token}` },
      });
      notifications.show({
        title: 'Success',
        message: 'Blog created successfully',
        color: 'green',
      });
      form.reset();
      fetchBlogs();
    } catch (error) {
      notifications.show({
        title: 'Error',
        message: 'Failed to create blog',
        color: 'red',
      });
    }
  };

  const handleDeleteBlog = async (id: number) => {
    try {
      await axios.delete(`http://localhost:8000/blog/${id}`, {
        headers: { Authorization: `Bearer ${token}` },
      });
      notifications.show({
        title: 'Success',
        message: 'Blog deleted successfully',
        color: 'green',
      });
      fetchBlogs();
    } catch (error) {
      notifications.show({
        title: 'Error',
        message: 'Failed to delete blog',
        color: 'red',
      });
    }
  };

  return (
    <Container size="lg" py="xl">
      <Group justify="space-between" mb="xl">
        <Title>Blog Dashboard</Title>
        <Button onClick={logout} color="red">Logout</Button>
      </Group>

      <Paper withBorder shadow="md" p="md" mb="xl">
        <Title order={2} mb="md">Create New Blog</Title>
        <form onSubmit={form.onSubmit(handleCreateBlog)}>
          <TextInput
            label="Title"
            placeholder="Enter blog title"
            required
            {...form.getInputProps('title')}
          />
          <Textarea
            label="Body"
            placeholder="Enter blog content"
            required
            minRows={3}
            mt="md"
            {...form.getInputProps('body')}
          />
          <Button type="submit" mt="md">Create Blog</Button>
        </form>
      </Paper>

      <Title order={2} mb="md">All Blogs</Title>
      <Grid>
        {blogs.map((blog) => (
          <Grid.Col key={blog.id} span={{ base: 12, sm: 6, lg: 4 }}>
            <Card shadow="sm" padding="lg" radius="md" withBorder>
              <Title order={3}>{blog.title}</Title>
              <Text c="dimmed" size="sm" mt="xs">
                By {blog.creator.name}
              </Text>
              <Text mt="sm">{blog.body}</Text>
              {blog.creator.email === localStorage.getItem('userEmail') && (
                <Button
                  color="red"
                  mt="md"
                  onClick={() => handleDeleteBlog(blog.id)}
                >
                  Delete
                </Button>
              )}
            </Card>
          </Grid.Col>
        ))}
      </Grid>
    </Container>
  );
}