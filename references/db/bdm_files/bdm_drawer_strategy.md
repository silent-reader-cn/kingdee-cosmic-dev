# 开票人设置-bdm_drawer_strategy

## 单据体-子表 t_bdm_drawer_item

- **表名称：** 单据体-子表
- **表名：** t_bdm_drawer_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | forg | 适用组织 | int8 | 64 |  | √ | 0 | [企业管理 bdm_org](../bdm_files/bdm_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bdm_drawer_item |  | fentryid |
| 2 | idx_bdm_drawer_item |  | fid |

---

## 开票人设置-主表 t_bdm_drawer_strategy

- **表名称：** 开票人设置-主表
- **表名：** t_bdm_drawer_strategy

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 策略名称 | varchar | 50 |  | √ | ' ' | 策略名称 |
| 4 | fdrawerstrategy | 开票人策略 | varchar | 50 |  | √ | ' ' | 开票人策略,枚举: |
| 5 | fdrawer | 开票人 | varchar | 50 |  | √ | ' ' | 开票人 |
| 6 | fpayee | 收款人 | varchar | 20 |  | √ | ' ' | 收款人 |
| 7 | freviewerid | 复核人主键 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | forgid | 组织id | int8 | 64 |  | √ | 0 | 组织id |
| 10 | fdrawerlist | 开票人列表 | varchar | 200 |  | √ | ' ' | 开票人列表 |
| 11 | fpriority | 优先级 | int4 | 32 |  | √ | 0 | 优先级 |
| 12 | ffilter_tag | 匹配条件_详情 | text | 0 |  |  | null | 匹配条件_详情 |
| 13 | fpayeeid | 收款人主键 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fdrawerid | 开票人主键 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | freviewer | 复核人 | varchar | 20 |  | √ | ' ' | 复核人 |
| 16 | ffilter | 匹配条件 | varchar | 255 |  | √ | ' ' | 匹配条件 |
| 17 | fnumber | 策略编号 | varchar | 50 |  | √ | ' ' | 策略编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bdm_drawer_strategy |  | forgid |
| 2 | pk_bdm_drawer_strategy |  | fid |
