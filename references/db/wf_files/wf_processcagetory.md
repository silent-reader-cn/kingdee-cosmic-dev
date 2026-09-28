# 流程分类-wf_processcagetory

## 流程分类-主表 t_wf_proccate

- **表名称：** 流程分类-主表
- **表名：** t_wf_proccate

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisleaf | 叶子节点 | bpchar | 1 |  | √ | '1' | 叶子节点 |
| 3 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 4 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fapplicationid | 应用ID | varchar | 36 |  | √ | ' ' | 应用ID |
| 6 | fparentid | 父id | int8 | 64 |  | √ | 0 | 父id |
| 7 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | 创建人 |
| 9 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 修改人 |
| 10 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 11 | fdescription | 描述 | varchar | 1024 |  | √ | ' ' | 描述 |
| 12 | fprocesstype | 流程类型 | varchar | 30 |  | √ | ' ' | 流程类型,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_proccate_parentid |  | fparentid |
| 2 | t_wf_proccate_pkey |  | fid |
| 3 | idx_wf_proccate_number |  | fnumber |

---

## 流程分类-多语言表 t_wf_proccate_l

- **表名称：** 流程分类-多语言表
- **表名：** t_wf_proccate_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 8 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 1024 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_proccate_localeid |  | fid,flocaleid |
| 2 | t_wf_proccate_l_pkey |  | fpkid |
