# 货补池使用规则-occba_occbarepuserule

## 使用组织分录-子表 t_occba_repruleuseorg

- **表名称：** 使用组织分录-子表
- **表名：** t_occba_repruleuseorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forgid | 组织编码 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occba_repruleuseorg_fid |  | fid |
| 2 | pk_occba_repruleuseorg |  | fentryid |

---

## 货补池使用规则-主表 t_occba_repuserule

- **表名称：** 货补池使用规则-主表
- **表名：** t_occba_repuserule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 3 | fname | 规则名称 | varchar | 150 |  | √ | ' ' | 规则名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fusebillconditionfilter | 使用单据条件 | varchar | 255 |  | √ | ' ' | 使用单据条件 |
| 6 | fusebillcondition | 使用单据条件 | varchar | 2000 |  | √ | ' ' | 使用单据条件 |
| 7 | forderlinetypeid | 货补行类型 | int8 | 64 |  | √ | 0 | [订单行类型 ocdbd_orderlinetype](../ocbsoc_files/ocdbd_orderlinetype.md) |
| 8 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 9 | frepuseconditionfilter | 货补池使用条件 | varchar | 255 |  | √ | ' ' | 货补池使用条件 |
| 10 | fpriority | 优先级 | int4 | 32 |  | √ | 0 | 优先级 |
| 11 | faudittime | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 12 | fusebillconditionfilter_tag | 使用单据条件_详情 | text | 0 |  |  | null | 使用单据条件_详情 |
| 13 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 14 | fstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | frepuseconditionfilter_tag | 货补池使用条件_详情 | text | 0 |  |  | null | 货补池使用条件_详情 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 18 | frepobjid | 货补池表 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 19 | fusebillobjid | 使用单据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 20 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | fnumber | 规则编号 | varchar | 80 |  | √ | ' ' | 规则编号 |
| 22 | frepusecondition | 货补池使用条件 | varchar | 2000 |  | √ | ' ' | 货补池使用条件 |
| 23 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occba_repuserule_number |  | fnumber |
| 2 | pk_occba_repuserule |  | fid |

---

## 货补匹配分录-子表 t_occba_repmatchentry

- **表名称：** 货补匹配分录-子表
- **表名：** t_occba_repmatchentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fusebillcol | 使用单据字段 | varchar | 100 |  | √ | ' ' | 使用单据字段 |
| 3 | fusebillcoltag | 使用单据字段标识 | varchar | 100 |  | √ | ' ' | 使用单据字段标识 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fcondition | 匹配条件 | varchar | 10 |  | √ | '=' | 匹配条件,枚举: = :等于 |
| 6 | frepcoltag | 货补池字段标识 | varchar | 100 |  | √ | ' ' | 货补池字段标识 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | frepcol | 货补池字段 | varchar | 100 |  | √ | ' ' | 货补池字段 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occba_repmatchentry |  | fentryid |
| 2 | idx_occba_repmatchentry_fid |  | fid |

---

## 货补池使用规则-多语言表 t_occba_repuserule_l

- **表名称：** 货补池使用规则-多语言表
- **表名：** t_occba_repuserule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 规则名称 | varchar | 150 |  | √ | ' ' | 规则名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occba_repuserule_l |  | fpkid |
| 2 | idx_occba_repuserule_l_flid |  | fid,flocaleid |
