# 来源标识配置-gai_sourcecode

## 来源标识配置-主表 t_gai_sourcecode

- **表名称：** 来源标识配置-主表
- **表名：** t_gai_sourcecode

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 标识名称 | varchar | 255 |  | √ | ' ' | 标识名称 |
| 3 | fbusinessid | 业务模块id | int8 | 64 |  | √ | 0 | 业务模块id |
| 4 | fbiztype | 模块类型 | varchar | 50 |  | √ | ' ' | 模块类型,枚举: PROCESS :任务流 AGENT :智能体 PROMPT :提示词 OLDREPODOC :旧文档知识库 OLDREPOSTRUCTURED :旧结构化知识库 NEWREPO :新知识库 |
| 5 | fcreatetime | 创建日期 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建日期 |
| 6 | fdesc | 标识描述 | varchar | 255 |  | √ | ' ' | 标识描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gai_sourcecode |  | fid |
| 2 | idx_gai_sourcecode_fname |  | fname |
