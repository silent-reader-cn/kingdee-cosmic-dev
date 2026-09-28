# 渠道仓位-ococic_location

## 渠道仓位-主表 t_ocdbd_location

- **表名称：** 渠道仓位-主表
- **表名：** t_ocdbd_location

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 仓库Id | int8 | 64 |  | √ | 0 | [渠道仓库 ococic_warehouse](../ococic_files/ococic_warehouse.md) |
| 2 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 3 | fname | fname | varchar | 80 |  | √ | ' ' |  |
| 4 | fseq | 序号 | int4 | 32 |  | √ | 0 | 序号 |
| 5 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 6 | fnumber | 仓位编码 | varchar | 80 |  | √ | ' ' | 仓位编码 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | ferplocationid | ERP仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 9 | fisdefault | 默认仓位 | bpchar | 1 |  | √ | '0' | 默认仓位 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_location_num |  | fnumber |
| 2 | pk_ocdbd_location |  | fentryid |

---

## 渠道仓位-多语言表 t_ocdbd_location_l

- **表名称：** 渠道仓位-多语言表
- **表名：** t_ocdbd_location_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 2 | fname | 仓位名称 | varchar | 80 |  | √ | ' ' | 仓位名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_location_l |  | fpkid |
| 2 | idx_ocdbd_locationl_elid |  | fentryid,flocaleid |
