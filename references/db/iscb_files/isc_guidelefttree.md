# 集成方案类别-isc_guidelefttree

## 集成方案类别-主表 t_isc_guidelefttree

- **表名称：** 集成方案类别-主表
- **表名：** t_isc_guidelefttree

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fconnsys2 | 连接系统2 | int8 | 64 |  | √ | 0 | [外部集成信息（废弃） isc_sysconn](../iscb_files/isc_sysconn.md) |
| 3 | fconnsys1 | 连接系统1 | int8 | 64 |  | √ | 0 | [外部集成信息（废弃） isc_sysconn](../iscb_files/isc_sysconn.md) |
| 4 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_guidelefttree_pkey |  | fid |
| 2 | idx_isc_guiltree_fnum |  | fnumber |

---

## 集成方案类别-多语言表 t_isc_guidelefttree_l

- **表名称：** 集成方案类别-多语言表
- **表名：** t_isc_guidelefttree_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 100 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_guidelefttree_l_pkey |  | fpkid |
| 2 | idx_isc_gltree_l_fid |  | fid,flocaleid |
