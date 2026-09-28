# 操作配置-er_operation

## 操作配置-多语言表 t_er_operation_l

- **表名称：** 操作配置-多语言表
- **表名：** t_er_operation_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  |  | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 备注 | varchar | 255 |  |  | ' ' | 备注 |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_er_operation_l |  | fpkid |
| 2 | idx_er_operation_l |  | fid,flocaleid |

---

## 操作配置-主表 t_er_operation

- **表名称：** 操作配置-主表
- **表名：** t_er_operation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsync | 是否拦截 | bpchar | 1 |  | √ | '0' | 是否拦截 |
| 3 | fsys | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 4 | fplugin | 插件 | varchar | 255 |  | √ | ' ' | 插件 |
| 5 | fnumber | 编号 | varchar | 80 |  | √ | ' ' | 编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_operation |  | fid |
| 2 | idx_t_er_operation |  | fplugin |
