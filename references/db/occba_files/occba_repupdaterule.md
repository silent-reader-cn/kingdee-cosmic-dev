# 货补池更新规则-occba_repupdaterule

## 货补池更新规则-多语言表 t_ocdbd_balrule_l

- **表名称：** 货补池更新规则-多语言表
- **表名：** t_ocdbd_balrule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_balrule_l |  | fpkid |
| 2 | idx_ocdbd_balrule_lcid |  | fid,flocaleid |

---

## 流水数据配置明细-子表 t_ocdbd_balruleflow

- **表名称：** 流水数据配置明细-子表
- **表名：** t_ocdbd_balruleflow

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fvaltype | 匹配方式 | bpchar | 1 |  | √ | '0' | 匹配方式,枚举: 1 :取源单字段 2 :固定值 0 :不匹配 |
| 3 | ffixedvaluetext | 固定值 | varchar | 255 |  | √ | ' ' | 固定值 |
| 4 | fflowcolname | 流水字段名称 | varchar | 100 |  | √ | ' ' | 流水字段名称 |
| 5 | ffixedvalue | 固定值 | varchar | 2000 |  | √ | ' ' | 固定值 |
| 6 | fcfgtips | 配置指引 | varchar | 255 |  | √ | ' ' | 配置指引 |
| 7 | fbillcolname | 来源单据字段名称 | varchar | 100 |  | √ | ' ' | 来源单据字段名称 |
| 8 | fbillcol | 来源单据字段标识 | varchar | 100 |  | √ | ' ' | 来源单据字段标识 |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fflowcol | 流水字段标识 | varchar | 50 |  | √ | ' ' | 流水字段标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_balruleflow |  | fid |
| 2 | pk_t_ocdbd_balruleflow |  | fentryid |

---

## 维度映射配置明细-子表 t_ocdbd_balruledim

- **表名称：** 维度映射配置明细-子表
- **表名：** t_ocdbd_balruledim

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fvaltype | 匹配方式 | bpchar | 1 |  | √ | '0' | 匹配方式,枚举: 1 :取源单字段 2 :系统默认值 3 :表达式计算 4 :固定值 0 :不匹配 |
| 3 | ffixedvaluetext | 固定值 | varchar | 255 |  | √ | ' ' | 固定值 |
| 4 | fdimexpr | 表达式 | varchar | 2000 |  | √ | ' ' | 表达式 |
| 5 | ffixedvalue | 固定值 | varchar | 2000 |  | √ | ' ' | 固定值 |
| 6 | fbalcolname | 余额表字段名称 | varchar | 100 |  | √ | ' ' | 余额表字段名称 |
| 7 | fbillcolname | 来源单据字段名称 | varchar | 100 |  | √ | ' ' | 来源单据字段名称 |
| 8 | fbillcol | 来源单据字段标识 | varchar | 100 |  | √ | ' ' | 来源单据字段标识 |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | fbalcol | 余额表字段标识 | varchar | 50 |  | √ | ' ' | 余额表字段标识 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_balruledim |  | fid |
| 2 | pk_ocdbd_balruledim |  | fentryid |

---

## 货补池更新规则-主表 t_ocdbd_balrule

- **表名称：** 货补池更新规则-主表
- **表名：** t_ocdbd_balrule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbalobjid | 资金池余额表 | varchar | 36 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 3 | fdatafilter | 数据筛选条件 | text | 0 |  |  | null | 数据筛选条件 |
| 4 | fpriority | 优先级 | int4 | 32 |  | √ | 0 | 优先级 |
| 5 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 6 | fnegativectrl | 更新余额负数控制 | bpchar | 1 |  | √ | '0' | 更新余额负数控制,枚举: 0 :不控制 1 :取消交易 |
| 7 | fflowobjid | 流水对象表 | varchar | 36 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 8 | fiswinter | 是否冬储 | bpchar | 1 |  | √ | '0' | 是否冬储 |
| 9 | fispreset | 是否预设 | bpchar | 1 |  | √ | '0' | 是否预设 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fupdatetype | 更新方向 | bpchar | 1 |  | √ | '0' | 更新方向,枚举: 0 :增加 1 :减少 |
| 17 | fautoreoprollback | 重复执行操作自动回滚 | bpchar | 1 |  | √ | '0' | 重复执行操作自动回滚 |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fsrcbillid | 来源单据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 20 | fupdateopval | 更新操作 | varchar | 200 |  | √ | ' ' | 更新操作 |
| 21 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 23 | fupdateopname | 更新操作 | varchar | 200 |  | √ | ' ' | 更新操作 |
| 24 | fdatafilterformula | 数据筛选条件 | text | 0 |  |  | null | 数据筛选条件 |
| 25 | fdatafilterformula_tag | 数据筛选条件_详情 | text | 0 |  |  | null | 数据筛选条件_详情 |
| 26 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 27 | frollbackopname | 回滚操作 | varchar | 200 |  | √ | ' ' | 回滚操作 |
| 28 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 29 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 30 | frollbackopval | 回滚操作 | varchar | 200 |  | √ | ' ' | 回滚操作 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_balrule |  | fid |
| 2 | idx_ocdbd_balrule |  | fnumber |

---

## 更新数据配置明细-子表 t_ocdbd_balruleupd

- **表名称：** 更新数据配置明细-子表
- **表名：** t_ocdbd_balruleupd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fvaltype | 更新方式 | bpchar | 1 |  | √ | '0' | 更新方式,枚举: 1 :取源单字段 0 :不更新 |
| 3 | fbalcolname | 余额表字段名称 | varchar | 100 |  | √ | ' ' | 余额表字段名称 |
| 4 | fisrollback | 是否回滚 | bpchar | 1 |  | √ | '0' | 是否回滚 |
| 5 | fbillcolname | 来源单据字段名称 | varchar | 100 |  | √ | ' ' | 来源单据字段名称 |
| 6 | fbillcol | 来源单据字段标识 | varchar | 50 |  | √ | ' ' | 来源单据字段标识 |
| 7 | fiscreateflow | 是否生成流水 | bpchar | 1 |  | √ | '0' | 是否生成流水 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fbalcol | 余额表字段标识 | varchar | 100 |  | √ | ' ' | 余额表字段标识 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_balruleupd |  | fid |
| 2 | pk_ocdbd_balruleupd |  | fentryid |
