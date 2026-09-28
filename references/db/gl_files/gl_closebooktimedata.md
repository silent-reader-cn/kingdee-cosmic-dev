# 公司结账时间详情-gl_closebooktimedata

## 公司结账时间详情-主表 t_gl_accountbookclosetime

- **表名称：** 公司结账时间详情-主表
- **表名：** t_gl_accountbookclosetime

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcompany | 公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fcloseday | 结账时间 | int8 | 64 |  | √ | 0 | 结账时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_gl_accountbookclosetime_pkey |  | fid |
| 2 | t_gl_accountbookclosetime_fcompany_key |  | fcompany |
