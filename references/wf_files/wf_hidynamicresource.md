# 历史动态流程资源-wf_hidynamicresource

## 历史动态流程资源-主表 t_wf_hidynresource

- **表名称：** 历史动态流程资源-主表
- **表名：** t_wf_hidynresource

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 70 |  | √ | ' ' | 名称 |
| 3 | factinstid | 活动实例ID | int8 | 64 |  | √ | 0 | 活动实例ID |
| 4 | fdeletereason | 删除原因 | varchar | 2000 |  | √ | ' ' | 删除原因 |
| 5 | fprocdefid | 流程定义ID | int8 | 64 |  | √ | 0 | 流程定义ID |
| 6 | factivityid | 活动节点ID | varchar | 255 |  | √ | ' ' | 活动节点ID |
| 7 | fprocinstid | 流程实例ID | int8 | 64 |  | √ | 0 | 流程实例ID |
| 8 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fduration | 耗时 | int8 | 64 |  | √ | 0 | 耗时 |
| 10 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型 |
| 11 | fmodifydate | 最后修改时间 | timestamp | 0 |  |  | null | 最后修改时间 |
| 12 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 13 | fcontent | fcontent | text | 0 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_wf_hidynresource_pkey |  | fid |
| 2 | idx_wf_hidynresource_type |  | ftype |
| 3 | idx_wf_hidynresource_proc |  | fprocdefid,fprocinstid |
| 4 | idx_wf_hidynresource_procinst |  | fprocinstid |

---

## 历史动态流程资源-多语言表 t_wf_hidynresource_l

- **表名称：** 历史动态流程资源-多语言表
- **表名：** t_wf_hidynresource_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 8 |  | √ | ' ' | localeid |
| 3 | fcontent | 资源内容 | text | 0 |  |  | null | 资源内容 |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_wf_hidynresource_l_pkey |  | fpkid |
| 2 | idx_wf_hidynresource_localeid |  | fid,flocaleid |
