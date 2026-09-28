# 返利计算方案-msrcs_rebateschema

## 判断标准分录-子表 t_msrcs_rebateschema_js

- **表名称：** 判断标准分录-子表
- **表名：** t_msrcs_rebateschema_js

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fjudgestandardid | 编码 | int8 | 64 |  | √ | 0 | [返利计算公式 msrcs_rebateformula](../msrcs_files/msrcs_rebateformula.md) |
| 3 | finterfacerule | 界面规则 | varchar | 50 |  | √ | ' ' | 界面规则,枚举: |
| 4 | fjudgesetting | 变量映射 | varchar | 2000 |  | √ | ' ' | 变量映射 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fispreset | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msrcs_rebateschemajs_fid |  | fid |
| 2 | pk_msrcs_rebateschema_js |  | fentryid |

---

## 返利计算方案-多语言表 t_msrcs_rebateschema_l

- **表名称：** 返利计算方案-多语言表
- **表名：** t_msrcs_rebateschema_l

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
| 1 | pk_msrcs_rebateschema_l |  | fpkid |
| 2 | idx_msrcs_rebateschemal_flid |  | fid,flocaleid |

---

## 界面规则单据体-子表 t_msrcs_interfacerule

- **表名称：** 界面规则单据体-子表
- **表名：** t_msrcs_interfacerule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finterfacename | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | finterfacecodition | 条件 | varchar | 2000 |  | √ | ' ' | 条件 |
| 4 | finterfaceid | 长整数 | int8 | 64 |  | √ | 0 | 长整数 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_msrcs_interfacerule |  | fentryid |
| 2 | idx_msrcs_interfacerule |  | fid |

---

## 数据源分录-子表 t_msrcs_rebateschema_se

- **表名称：** 数据源分录-子表
- **表名：** t_msrcs_rebateschema_se

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqfitlerstr_tag | 取数条件(字符串)_详情 | text | 0 |  |  | null | 取数条件(字符串)_详情 |
| 3 | fqfitlerstr | 取数条件(字符串) | varchar | 2000 |  | √ | ' ' | 取数条件(字符串) |
| 4 | fsrcbillid | 来源单据 | varchar | 40 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 5 | frebatesourceid | 数据源编码 | varchar | 80 |  | √ | ' ' | [返利计算数据源 msrcs_rebatesource](../msrcs_files/msrcs_rebatesource.md) |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fenable | 可用状态 | bpchar | 1 |  | √ | '1' | 可用状态,枚举: 0 :禁用 1 :可用 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fispreset | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msrcs_rebateschemase_fid |  | fid |
| 2 | pk_msrcs_rebateschema_se |  | fentryid |

---

## 界面规则单据体-多语言表 t_msrcs_interfacerule_l

- **表名称：** 界面规则单据体-多语言表
- **表名：** t_msrcs_interfacerule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | finterfacename | 名称 | varchar | 250 |  | √ | ' ' | 名称 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_msrcs_interfacerule_l |  | fpkid |
| 2 | idx_msrcs_interfacerule_l |  | fentryid,flocaleid |

---

## 计算公式分录-子表 t_msrcs_rebateschema_cf

- **表名称：** 计算公式分录-子表
- **表名：** t_msrcs_rebateschema_cf

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finterfacerule | 界面规则 | varchar | 50 |  | √ | ' ' | 界面规则,枚举: |
| 3 | fcalformulaid | 编码 | int8 | 64 |  | √ | 0 | [返利计算公式 msrcs_rebateformula](../msrcs_files/msrcs_rebateformula.md) |
| 4 | fcalformulasetting | 变量映射 | varchar | 2000 |  | √ | ' ' | 变量映射 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | frowamtmode | 分摊方式 | int8 | 64 |  | √ | 0 | [返利行金额计算方式 msrcs_rowamtmode](../msrcs_files/msrcs_rowamtmode.md) |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fispreset | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msrcs_rebateschemacf_fid |  | fid |
| 2 | pk_msrcs_rebateschema_cf |  | fentryid |

---

## 返利对象单据体-子表 t_msrcs_rebateschemaobj

- **表名称：** 返利对象单据体-子表
- **表名：** t_msrcs_rebateschemaobj

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcobjfield | 返利对象字段Key | varchar | 250 |  | √ | ' ' | 返利对象字段Key |
| 3 | ftargetobjfield | 返利对象字段Key | varchar | 250 |  | √ | ' ' | 返利对象字段Key |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | frebateclassid | 返利类别 | int8 | 64 |  | √ | 0 | [返利类别 msrcs_rebateclass](../msrcs_files/msrcs_rebateclass.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_msrcs_rebateschemaobj |  | fentryid |
| 2 | idx_msrcs_rebateschemaobj |  | fid |

---

## 返利计算方案-主表 t_msrcs_rebateschema

- **表名称：** 返利计算方案-主表
- **表名：** t_msrcs_rebateschema

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 说明 | varchar | 255 |  | √ | ' ' | 说明 |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fschemefilter | 执行条件存储字段 | varchar | 2000 |  | √ | ' ' | 执行条件存储字段 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fpolicyobj | 政策对象 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 9 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | frebatemodelid | 返利计算模型 | varchar | 40 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 13 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 15 | fissyspreset | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_msrcs_rebateschema |  | fid |
| 2 | idx_msrcs_rebateschema_num |  | fnumber |

---

## 查询条件匹配规则-子表 t_msrcs_schema_qcond

- **表名称：** 查询条件匹配规则-子表
- **表名：** t_msrcs_schema_qcond

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmatchplugin | 自定义匹配插件 | varchar | 255 |  | √ | ' ' | 自定义匹配插件 |
| 3 | fmodelcol | 数据源字段key | varchar | 150 |  | √ | ' ' | 数据源字段key |
| 4 | fconditiontype | 条件类型 | bpchar | 1 |  | √ | ' ' | 条件类型,枚举: A :全局条件 B :分组条件（政策） C :分组条件（条件组） |
| 5 | fmatchmode | 匹配方式 | varchar | 10 |  | √ | ' ' | 匹配方式,枚举: = :等于 > :大于 >= :大于等于 < :小于 <= :小于等于 in :在…中 cus :自定义 |
| 6 | fpolicycol | 政策字段标识 | varchar | 150 |  | √ | ' ' | 政策字段标识 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msrcs_schema_qcond |  | fid |
| 2 | pk_msrcs_schema_qcond |  | fentryid |

---

## 返利预提公式分录-子表 t_msrcs_rebateschema_ac

- **表名称：** 返利预提公式分录-子表
- **表名：** t_msrcs_rebateschema_ac

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finterfacerule | 界面规则 | varchar | 50 |  | √ | ' ' | 界面规则,枚举: |
| 3 | faccrueformula | 编码 | int8 | 64 |  | √ | 0 | [返利计算公式 msrcs_rebateformula](../msrcs_files/msrcs_rebateformula.md) |
| 4 | fcshowname | fcshowname | varchar | 80 |  | √ | ' ' |  |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | frowamtmode | 分摊方式 | int8 | 64 |  | √ | 0 | [返利行金额计算方式 msrcs_rowamtmode](../msrcs_files/msrcs_rowamtmode.md) |
| 7 | faccrueispreset | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | faccrueformulasetting | 变量映射 | varchar | 2000 |  | √ | ' ' | 变量映射 |
| 10 | fispreset | fispreset | bpchar | 1 |  | √ | '0' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_msrcs_rebateschema_ac |  | fentryid |
| 2 | idx_msrcs_rebateschemaac_fid |  | fid |
