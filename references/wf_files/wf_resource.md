# 流程资源-wf_resource

## 流程资源-主表 t_wf_gebytearray

- **表名称：** 流程资源-主表
- **表名：** t_wf_gebytearray

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fcurrentlanguage | 当前语言 | varchar | 8 |  | √ | ' ' | 当前语言 |
| 4 | fgenerated | 是否是引擎生成 | bpchar | 1 |  | √ | '0' | 是否是引擎生成 |
| 5 | fcontent | 资源数据 | text | 0 |  |  | null | 资源数据 |
| 6 | fdeploymentid | 部署ID | int8 | 64 |  | √ | 0 | 部署ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_gebytearray_dpy |  | fdeploymentid |
| 2 | t_wf_gebytearray_pkey |  | fid |

---

## 流程资源-多语言表 t_wf_gebytearray_l

- **表名称：** 流程资源-多语言表
- **表名：** t_wf_gebytearray_l

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
| 1 | idx_wf_gebytearray_localeid |  | fid,flocaleid |
| 2 | t_wf_gebytearray_l_pkey |  | fpkid |
