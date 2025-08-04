# Contributing Guidelines

Thank you for your interest in contributing to the Awesome Docker Resources list! This document provides guidelines and instructions for contributing.

## 🤝 How to Contribute

### 1. Fork and Clone
- Fork this repository to your GitHub account
- Clone your fork locally:
  ```bash
  git clone https://github.com/YOUR_USERNAME/docker-offload-resources.git
  cd docker-offload-resources
  ```

### 2. Create a Branch
Create a new branch for your contribution:
```bash
git checkout -b add-awesome-resource
```

### 3. Make Your Changes
Add your resource to the appropriate section in the README.md file.

### 4. Commit and Push
Commit your changes with a descriptive message:
```bash
git add .
git commit -m "Add [Resource Name] to [Category] section"
git push origin add-awesome-resource
```

### 5. Create a Pull Request
- Go to your fork on GitHub
- Click "New Pull Request"
- Provide a clear title and description
- Submit the pull request

## 📋 Contribution Guidelines

### What Makes a Good Resource?
- **High Quality**: The resource should provide significant value to Docker users
- **Up-to-date**: Resources should be current and maintained
- **Accessible**: Links should be working and publicly accessible
- **Relevant**: Must be directly related to Docker, containers, or the ecosystem
- **Unique**: Avoid duplicate resources already listed

### Categories
Resources should be added to the most appropriate category:
- **Official Documentation**: Official Docker resources only
- **Getting Started**: Beginner-friendly tutorials and guides
- **Tutorials and Guides**: In-depth learning materials
- **Books**: Published books (free or commercial)
- **Blogs and Articles**: Blog posts and articles
- **Videos and YouTube Channels**: Video content and channels
- **Tools and Utilities**: Software tools and utilities
- **Security**: Security-focused resources
- **Best Practices**: Guidelines and best practices
- **Docker Compose**: Compose-specific resources
- **Orchestration**: Container orchestration platforms
- **Performance and Monitoring**: Monitoring and performance tools
- **Development and CI/CD**: Development and deployment tools
- **Multi-Architecture**: Cross-platform and ARM resources
- **Community Resources**: Forums, communities, events

### Format Requirements

#### Link Format
```markdown
- [Resource Name](https://link-to-resource.com) - Brief description of what the resource offers
```

#### Description Guidelines
- Keep descriptions concise (1-2 sentences max)
- Start with what the resource *is* or *does*
- Avoid promotional language
- Use sentence case, not title case
- End descriptions with a period

#### Examples
✅ **Good**:
```markdown
- [Portainer](https://www.portainer.io/) - Web-based Docker management interface with intuitive UI
- [Docker Deep Dive](https://github.com/nigelpoulton/docker-deep-dive) - Comprehensive guide from basics to advanced topics
```

❌ **Bad**:
```markdown
- [Awesome Tool](https://example.com) - THE BEST Docker tool ever created!!!
- [Some Resource](https://example.com) - A resource
```

### What Not to Include
- **Broken Links**: Always verify links work before submitting
- **Promotional Content**: Avoid overly promotional or sales-focused content
- **Outdated Resources**: Resources that haven't been updated in 2+ years
- **Low-Quality Content**: Poorly written or superficial content
- **Duplicate Resources**: Check if the resource is already listed
- **Non-English Resources**: Unless they provide unique value not available in English
- **Personal Blogs**: Unless they contain high-quality, comprehensive Docker content

## 🔍 Review Process

### What We Look For
1. **Link Quality**: Working links to high-quality resources
2. **Categorization**: Resources placed in appropriate categories
3. **Description Quality**: Clear, helpful descriptions
4. **Formatting**: Proper markdown formatting
5. **Uniqueness**: New resources not already listed

### Response Time
- We aim to review pull requests within 1 week
- Complex contributions may take longer
- You may be asked to make changes based on feedback

## 📝 Content Standards

### Language and Tone
- Use clear, professional language
- Avoid jargon without explanation
- Be inclusive and welcoming
- Maintain neutrality (avoid bias toward specific tools/companies)

### Technical Accuracy
- Ensure technical information is correct
- Verify compatibility and version information
- Include relevant prerequisites or limitations

### Maintenance
- Resources should be actively maintained
- Prefer resources with recent updates (within 12 months)
- Note if a resource is archived or deprecated

## 🐛 Reporting Issues

### Found a Problem?
If you find broken links, outdated information, or other issues:

1. **Check if it's already reported** in the Issues tab
2. **Create a new issue** with:
   - Clear description of the problem
   - Link to the problematic resource
   - Suggested fix (if applicable)

### Types of Issues to Report
- Broken or redirected links
- Outdated information
- Inappropriate content
- Categorization problems
- Formatting issues

## 🏆 Recognition

Contributors will be recognized in the following ways:
- Listed in the repository contributors
- GitHub contribution activity
- Special mention for significant contributions

## 📞 Getting Help

Need help with your contribution?
- Create an issue with the "question" label
- Check existing issues for similar questions
- Review this guide thoroughly first

## 📋 Commit Message Guidelines

Use clear, descriptive commit messages:

### Format
```
[Action] [Resource Name] to [Section]

Optional longer description if needed.
```

### Examples
- `Add Portainer to Tools section`
- `Update Docker Compose documentation link`
- `Fix broken link in Security section`
- `Remove outdated resource from Tutorials`

## ✅ Pre-submission Checklist

Before submitting your pull request:

- [ ] Link is working and accessible
- [ ] Resource is high-quality and relevant
- [ ] Proper category selected
- [ ] Description follows format guidelines
- [ ] No duplicate resources
- [ ] Markdown formatting is correct
- [ ] Commit message is descriptive
- [ ] Changes have been tested locally

## 🎯 Quality Standards

We maintain high standards to keep this list valuable:

### Minimum Requirements
- Resource must be directly Docker-related
- Content must be in English (with rare exceptions)
- Links must be publicly accessible
- Resource should be actively maintained
- Content must provide educational or practical value

### Preferred Qualities
- Recent updates (within 12 months)
- Comprehensive coverage of topics
- Clear, well-written content
- Good community reputation
- Free and open access

Thank you for helping make this the best Docker resource list on GitHub! 🐳

## 📄 License

By contributing to this project, you agree that your contributions will be licensed under the MIT License.
