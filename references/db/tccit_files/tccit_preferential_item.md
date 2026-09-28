# 优惠项目取数规则-tccit_preferential_item

## 优惠项目取数规则-主表 t_tccit_preferential_item

- **表名称：** 优惠项目取数规则-主表
- **表名：** t_tccit_preferential_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | forgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fruletype | 规则类型 | varchar | 30 |  | √ | ' ' | 规则类型,枚举: private :自用规则 public :可分配规则 |
| 6 | fbusinessfeature | 业务特性 | varchar | 30 |  | √ | ' ' | 业务特性,枚举: 1 :以发票口径为应税销售额 2 :以会计口径为应税销售额 4 :以发票和会计口径孰大原则确认应税销售额 |
| 7 | flevytype | 征收方式 | varchar | 50 |  | √ | ' ' | 征收方式,枚举: czzs :查账征收 hdzs :核定征收 |
| 8 | fdatefield | 第一笔项目收入年度 | timestamp | 0 |  |  | null | 第一笔项目收入年度 |
| 9 | fitemid | 优惠项目选择 | int8 | 64 |  | √ | 0 | 优惠项目（树） tpo_discount_tree |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | ftype | 优惠类型 | varchar | 30 |  | √ | ' ' | 优惠类型,枚举: 1 :免税收入 2 :减计收入 3 :所得减免 |
| 15 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 17 | frulepurpose | 规则用途 | varchar | 50 |  | √ | ' ' | 规则用途,枚举: nssb :纳税申报 sjjt :税金计提 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_preferential_item |  | forgid |
| 2 | t_tccit_preferential_item_pkey |  | fid |

---

## 优惠项目取数规则-多语言表 t_tccit_preferential_item_l

- **表名称：** 优惠项目取数规则-多语言表
- **表名：** t_tccit_preferential_item_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 项目名称 | varchar | 100 |  | √ | ' ' | 项目名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_preferential_item_l |  | fid,flocaleid |
| 2 | t_tccit_preferential_item_l_pkey |  | fpkid |

---

## 取数规则-子表 t_tccit_item_entry

- **表名称：** 取数规则-子表
- **表名：** t_tccit_item_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffconditionjson | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 3 | fexratejson | 汇率转换 | varchar | 255 |  | √ | ' ' | 汇率转换 |
| 4 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | [数据源字段配置 tctb_datasource_entry](../tctb_files/tctb_datasource_entry.md) |
| 5 | fadvancedconfjson | 取数逻辑 | text | 0 |  |  | null | 取数逻辑 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fbizname | 业务名称 | varchar | 50 |  | √ | ' ' | 业务名称 |
| 8 | ftable | 数据源 | int8 | 64 |  | √ | 0 | [数据源配置 tctb_custom_datasource](../tctb_files/tctb_custom_datasource.md) |
| 9 | fabsolute | 绝对值 | bpchar | 1 |  | √ | ' ' | 绝对值 |
| 10 | fiscustomtable | fiscustomtable | bpchar | 1 |  | √ | ' ' |  |
| 11 | fadvancedconf | 取数逻辑 | text | 0 |  |  | null | 取数逻辑 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | ffiltercondition | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 14 | fdatadirection | 取数方向 | varchar | 30 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 15 | fdatatype | 取数方式 | varchar | 30 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 jsflqs :价税分离取数 cysldsqs :除以税率倒算取数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tccit_item_entry_pkey |  | fentryid |
| 2 | idx_tccit_item_entry |  | fid |
