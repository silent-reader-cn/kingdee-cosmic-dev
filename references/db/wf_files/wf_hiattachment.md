# 附件-wf_hiattachment

## 附件-多语言表 t_wf_hiattachment_l

- **表名称：** 附件-多语言表
- **表名：** t_wf_hiattachment_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 8 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_hiattachment_localeid |  | fid,flocaleid |
| 2 | t_wf_hiattachment_l_pkey |  | fpkid |

---

## 附件-主表 t_wf_hiattachment

- **表名称：** 附件-主表
- **表名：** t_wf_hiattachment

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | furlid | 链接地址id | int8 | 64 |  | √ | 0 | 链接地址id |
| 3 | fcontentid | 内容ID | int8 | 64 |  | √ | 0 | 内容ID |
| 4 | fname | fname | varchar | 255 |  | √ | ' ' |  |
| 5 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型 |
| 7 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fuserid | 用户ID | int8 | 64 |  | √ | 0 | 用户ID |
| 9 | fprocinstid | 流程实例ID | int8 | 64 |  | √ | 0 | 流程实例ID |
| 10 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 11 | ftaskid | 任务ID | int8 | 64 |  | √ | 0 | 任务ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_hiattachment_contid |  | fcontentid |
| 2 | idx_wf_hiattachment_proc |  | fprocinstid |
| 3 | idx_wf_hiattachment_task |  | ftaskid |
| 4 | t_wf_hiattachment_pkey |  | fid |
