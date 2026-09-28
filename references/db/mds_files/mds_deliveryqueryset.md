# 发货查询方案-mds_deliveryqueryset

## 发货查询方案-主表 t_mds_deliveryqueryset

- **表名称：** 发货查询方案-主表
- **表名：** t_mds_deliveryqueryset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fjobid | 作业号 | varchar | 50 |  | √ | ' ' | 作业号 |
| 6 | fresult | 运算结果 | varchar | 5 |  | √ | ' ' | 运算结果,枚举: A :运算成功 B :运算失败 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fplanid | 任务号 | varchar | 50 |  | √ | ' ' | 任务号 |
| 9 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | flastruntime | 最后一次运算时间 | timestamp | 0 |  |  | null | 最后一次运算时间 |
| 13 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 15 | fsetval | 设置数据 | varchar | 2000 |  | √ | ' ' | 设置数据 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mds_deliveryqueryset |  | fid |
| 2 | idx_mds_deliveryqueryset_num |  | fnumber |

---

## 发货数据源配置-子表 t_mds_resourceentry

- **表名称：** 发货数据源配置-子表
- **表名：** t_mds_resourceentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fuse | 启用 | bpchar | 1 |  | √ | '0' | 启用 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fresource | 数据源编码 | int8 | 64 |  | √ | 0 | [数据源配置 mrp_resource_dataconf_rgt](../msplan_files/mrp_resource_dataconf_rgt.md) |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fdeliverytype | 发货类型 | varchar | 5 |  | √ | ' ' | 发货类型,枚举: 0 :销售出库 1 :生产领料 2 :其他出库 3 :直接调拨 4 :分步调拨 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mds_resourceentry |  | fentryid |
| 2 | idx_mds_resourceentry_fk |  | fid |

---

## 发货查询方案-多语言表 t_mds_deliveryqueryset_l

- **表名称：** 发货查询方案-多语言表
- **表名：** t_mds_deliveryqueryset_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mds_deliveryqueryset_l |  | fid,flocaleid |
| 2 | pk_mds_deliveryqueryset_l |  | fpkid |
