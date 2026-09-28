# 留抵退税规则-tcvat_rule_refund

## 全部不含税销售额取数配置-子表 t_tcvat_refund_qbbhsxse

- **表名称：** 全部不含税销售额取数配置-子表
- **表名：** t_tcvat_refund_qbbhsxse

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentryentityconf | 取数逻辑 | varchar | 2000 |  | √ | ' ' | 取数逻辑 |
| 3 | fexratejson | 汇率转换 | varchar | 500 |  | √ | ' ' | 汇率转换 |
| 4 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | 数据源字段配置 tctb_datasource_entry |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fbizname | 业务名称 | varchar | 100 |  | √ | ' ' | 业务名称 |
| 7 | fconditionjson | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 8 | fentryentityconfjson | 增值税税率/征收率 | varchar | 2000 |  | √ | ' ' | 增值税税率/征收率 |
| 9 | ftable | 数据源 | int8 | 64 |  | √ | 0 | 数据源配置 tctb_custom_datasource |
| 10 | fabsolute | 绝对值 | bpchar | 1 |  | √ | '0' | 绝对值 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | ffiltercondition | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 13 | fdatadirection | 取数方向 | varchar | 50 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 14 | fdatatype | 取数方式 | varchar | 50 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 jsflqs :含税价换算不含税价 cysldsqs :税额换算不含税价 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_refund_qbbhsxse |  | fentryid |
| 2 | idx_tcvat_refund_qbbhsxse_fk |  | fid |

---

## 特定行业不含税销售额取数配置-子表 t_tcvat_refund_tdhybhs

- **表名称：** 特定行业不含税销售额取数配置-子表
- **表名：** t_tcvat_refund_tdhybhs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentryentityconf | 取数逻辑 | varchar | 2000 |  | √ | ' ' | 取数逻辑 |
| 3 | fexratejson | 汇率转换 | varchar | 500 |  | √ | ' ' | 汇率转换 |
| 4 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | 数据源字段配置 tctb_datasource_entry |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fbizname | 业务名称 | varchar | 100 |  | √ | ' ' | 业务名称 |
| 7 | fconditionjson | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 8 | fentryentityconfjson | 增值税税率/征收率 | varchar | 2000 |  | √ | ' ' | 增值税税率/征收率 |
| 9 | ftable | 数据源 | int8 | 64 |  | √ | 0 | 数据源配置 tctb_custom_datasource |
| 10 | fabsolute | 绝对值 | bpchar | 1 |  | √ | '0' | 绝对值 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | ffiltercondition | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 13 | fdatadirection | 取数方向 | varchar | 50 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 14 | fdatatype | 取数方式 | varchar | 50 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 jsflqs :含税价换算不含税价 cysldsqs :税额换算不含税价 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvat_refund_tdhybhs_fk |  | fid |
| 2 | pk_tcvat_refund_tdhybhs |  | fentryid |

---

## 上年度末资产总额取数配置-子表 t_tcvat_refund_sndmzcze

- **表名称：** 上年度末资产总额取数配置-子表
- **表名：** t_tcvat_refund_sndmzcze

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffconditionjson | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 3 | fentryentityconf | 取数逻辑 | varchar | 2000 |  | √ | ' ' | 取数逻辑 |
| 4 | fexratejson | 汇率转换 | varchar | 500 |  | √ | ' ' | 汇率转换 |
| 5 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | 数据源字段配置 tctb_datasource_entry |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fbizname | 业务名称 | varchar | 100 |  | √ | ' ' | 业务名称 |
| 8 | fentryentityconfjson | 增值税税率/征收率 | varchar | 2000 |  | √ | ' ' | 增值税税率/征收率 |
| 9 | ftable | 数据源 | int8 | 64 |  | √ | 0 | 数据源配置 tctb_custom_datasource |
| 10 | fabsolute | 绝对值 | bpchar | 1 |  | √ | '0' | 绝对值 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | ffiltercondition | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 13 | fdatadirection | 取数方向 | varchar | 50 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 14 | fdatatype | 取数方式 | varchar | 50 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_refund_sndmzcze |  | fentryid |
| 2 | idx_tcvat_refund_sndmzcze_fk |  | fid |

---

## 留抵退税规则-主表 t_tcvat_rule_refund

- **表名称：** 留抵退税规则-主表
- **表名：** t_tcvat_rule_refund

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 业务名称 | varchar | 100 |  | √ | ' ' | 业务名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fruletype | 规则类型 | varchar | 50 |  | √ | ' ' | 规则类型,枚举: private :自用规则 public :可分配规则 |
| 7 | frefundtype | 退税企业类型 | int8 | 64 |  | √ | 0 | 税务辅助数据 tpo_tcvat_assist |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fissystem | 系统预设 | varchar | 50 |  | √ | ' ' | 系统预设,枚举: 0 :否 1 :是 |
| 13 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 规则编码 | varchar | 30 |  | √ | ' ' | 规则编码 |
| 15 | frulepurpose | 规则用途 | varchar | 50 |  | √ | ' ' | 规则用途,枚举: nssb :纳税申报 sjjt :税金计提 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_rule_refund |  | fid |
| 2 | idx_taxc_rule_refund_org |  | forgid |

---

## 留抵退税规则-多语言表 t_tcvat_rule_refund_l

- **表名称：** 留抵退税规则-多语言表
- **表名：** t_tcvat_rule_refund_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 业务名称 | varchar | 100 |  | √ | ' ' | 业务名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvat_rule_refund_l_0 |  | fid,flocaleid |
| 2 | pk_tcvat_rule_refund_l |  | fpkid |
