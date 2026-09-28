# 出库规则配置-bd_matchout_rule

## 出库规则配置-多语言表 t_bd_matchout_rule_l

- **表名称：** 出库规则配置-多语言表
- **表名：** t_bd_matchout_rule_l

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
| 1 | idx_bd_matchoutrule_l_fid |  | fid,flocaleid |
| 2 | pk_t_bd_matchout_rule_l |  | fpkid |

---

## 出库规则配置-主表 t_bd_matchout_rule

- **表名称：** 出库规则配置-主表
- **表名：** t_bd_matchout_rule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 数据状态 | varchar | 5 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fenable | 使用状态 | varchar | 5 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 9 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 10 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bd_matchout_rule |  | fid |
| 2 | idx_bd_matchoutrule_number |  | fnumber |

---

## 排序规则-子表 t_bd_matchout_order

- **表名称：** 排序规则-子表
- **表名：** t_bd_matchout_order

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcustomorder | 自定义排序 | varchar | 500 |  | √ | ' ' | 自定义排序 |
| 3 | ftype | 排序方式 | varchar | 50 |  | √ | 'asc' | 排序方式,枚举: asc :升序 desc :降序 custom :自定义 project :跨项目领料 sdkplugin :SDK插件 |
| 4 | fvalueouttype | 空值出库规则 | bpchar | 1 |  | √ | 'A' | 空值出库规则,枚举: A :默认 B :优先出库 C :延后出库 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fsource | 字段来源 | varchar | 50 |  | √ | 'im_inv_realbalance' | 字段来源,枚举: im_inv_realbalance :即时库存余额表 im_lotintrack :批号入库跟踪表 |
| 8 | fsrccolname | 排序字段名称 | varchar | 300 |  | √ | ' ' | 排序字段名称 |
| 9 | fsrccol | 排序字段标识 | varchar | 100 |  | √ | ' ' | 排序字段标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_matchoutorder_id |  | fid |
| 2 | pk_t_bd_matchout_order |  | fentryid |
