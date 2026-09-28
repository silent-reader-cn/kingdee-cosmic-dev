# 任务中心导航栏-wf_tasknavigation

## 任务中心导航栏-主表 t_wf_navigation

- **表名称：** 任务中心导航栏-主表
- **表名：** t_wf_navigation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaskcenterruleid | 任务规则id | int8 | 64 |  | √ | 0 | 任务规则id |
| 3 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 4 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fparentid | 父id | int8 | 64 |  | √ | 0 | 父id |
| 6 | fmodifydate | 最后修改时间 | timestamp | 0 |  |  | null | 最后修改时间 |
| 7 | factivitstate | 启用状态 | varchar | 100 |  | √ | ' ' | 启用状态 |
| 8 | fuserid | 用户id | int8 | 64 |  | √ | 0 | 用户id |
| 9 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_wf_navigation_pkey |  | fid |
| 2 | idx_wf_navigation_create |  | fcreatedate |

---

## 任务中心导航栏-多语言表 t_wf_navigation_l

- **表名称：** 任务中心导航栏-多语言表
- **表名：** t_wf_navigation_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 8 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_wf_navigation_l_pkey |  | fpkid |
| 2 | idx_wf_navigation_localeid |  | fid,flocaleid |
