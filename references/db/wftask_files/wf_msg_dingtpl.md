# 钉钉模板-wf_msg_dingtpl

## 钉钉模板-主表 t_wf_dingtpl

- **表名称：** 钉钉模板-主表
- **表名：** t_wf_dingtpl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftplid | 钉钉模板ID | varchar | 200 |  | √ | ' ' | 钉钉模板ID |
| 3 | fagentid | 应用标识 | int8 | 64 |  | √ | 0 | 应用标识 |
| 4 | fentityname | 单据名称 | varchar | 200 |  | √ | ' ' | 单据名称 |
| 5 | fcorpid | 企业标识 | varchar | 50 |  | √ | ' ' | 企业标识 |
| 6 | ftpldescription | 模板描述 | varchar | 500 |  | √ | ' ' | 模板描述 |
| 7 | fentitynumber | 单据编码 | varchar | 100 |  | √ | ' ' | 单据编码 |
| 8 | ftplname | 模板名称 | varchar | 200 |  | √ | ' ' | 模板名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_dingtpl |  | fentitynumber |
| 2 | t_wf_dingtpl_pkey |  | fid |

---

## 钉钉模板-多语言表 t_wf_dingtpl_l

- **表名称：** 钉钉模板-多语言表
- **表名：** t_wf_dingtpl_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentityname | 单据名称 | varchar | 200 |  | √ | ' ' | 单据名称 |
| 3 | ftpldescription | 模板描述 | varchar | 500 |  | √ | ' ' | 模板描述 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | ftplname | 模板名称 | varchar | 200 |  | √ | ' ' | 模板名称 |
| 6 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_dingtpl_l |  | fid,flocaleid |
| 2 | t_wf_dingtpl_l_pkey |  | fpkid |
