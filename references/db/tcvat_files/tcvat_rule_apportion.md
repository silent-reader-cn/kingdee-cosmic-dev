# 进项转出比例分摊台账-tcvat_rule_apportion

## 当期简易计税方法计税销售额-子表 t_tcvat_rule_apt_jyjs

- **表名称：** 当期简易计税方法计税销售额-子表
- **表名：** t_tcvat_rule_apt_jyjs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | 数据源字段配置 tctb_datasource_entry |
| 3 | fentryentity11confjson | 增值税税率/预征率 | varchar | 2000 |  | √ | ' ' | 增值税税率/预征率 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fbizname | 业务名称 | varchar | 50 |  | √ | ' ' | 业务名称 |
| 6 | fconditionjson | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 7 | fentryentity11conf | 取数逻辑 | varchar | 2000 |  | √ | ' ' | 取数逻辑 |
| 8 | ftable | 数据源 | int8 | 64 |  | √ | 0 | 数据源配置 tctb_custom_datasource |
| 9 | fabsolute | 绝对值 | bpchar | 1 |  | √ | '0' | 绝对值 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | ffiltercondition | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 12 | fdatadirection | 取数方向 | varchar | 50 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 13 | fdatatype | 取数方式 | varchar | 50 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 jsflqs :含税价换算不含税价 cysldsqs :税额换算不含税价 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_rule_apt_jyjs |  | fentryid |
| 2 | idx_tcvat_rule_apt_jyjs_fk |  | fid |

---

## 当期免税项目销售额-子表 t_tcvat_rule_apt_msxm

- **表名称：** 当期免税项目销售额-子表
- **表名：** t_tcvat_rule_apt_msxm

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | 数据源字段配置 tctb_datasource_entry |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fbizname | 业务名称 | varchar | 50 |  | √ | ' ' | 业务名称 |
| 5 | fconditionjson | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 6 | ftable | 数据源 | int8 | 64 |  | √ | 0 | 数据源配置 tctb_custom_datasource |
| 7 | fabsolute | 绝对值 | bpchar | 1 |  | √ | '0' | 绝对值 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | ffiltercondition | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 10 | fentryentity12confjson | 增值税税率/征收率 | varchar | 2000 |  | √ | ' ' | 增值税税率/征收率 |
| 11 | fdatadirection | 取数方向 | varchar | 50 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 12 | fentryentity12conf | 取数逻辑 | varchar | 2000 |  | √ | ' ' | 取数逻辑 |
| 13 | fdatatype | 取数方式 | varchar | 50 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 jsflqs :含税价换算不含税价 cysldsqs :税额换算不含税价 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvat_rule_apt_msxm_fk |  | fid |
| 2 | pk_tcvat_rule_apt_msxm |  | fentryid |

---

## 当期全部销售额-子表 t_tcvat_rule_apt_dqqb

- **表名称：** 当期全部销售额-子表
- **表名：** t_tcvat_rule_apt_dqqb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentryentity1conf | 取数逻辑 | varchar | 2000 |  | √ | ' ' | 取数逻辑 |
| 3 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | 数据源字段配置 tctb_datasource_entry |
| 4 | fentryentity1confjson | 增值税税率/预征率 | varchar | 2000 |  | √ | ' ' | 增值税税率/预征率 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fbizname | 业务名称 | varchar | 50 |  | √ | ' ' | 业务名称 |
| 7 | fconditionjson | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 8 | ftable | 数据源 | int8 | 64 |  | √ | 0 | 数据源配置 tctb_custom_datasource |
| 9 | fabsolute | 绝对值 | bpchar | 1 |  | √ | '0' | 绝对值 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | ffiltercondition | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 12 | fdatadirection | 取数方向 | varchar | 50 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 13 | fdatatype | 取数方式 | varchar | 50 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 jsflqs :含税价换算不含税价 cysldsqs :税额换算不含税价 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_rule_apt_dqqb |  | fentryid |
| 2 | idx_tcvat_rule_apt_dqqb_fk |  | fid |

---

## 进项转出比例分摊台账-多语言表 t_tcvat_rule_apportion_l

- **表名称：** 进项转出比例分摊台账-多语言表
- **表名：** t_tcvat_rule_apportion_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvat_rule_apportion_l_0 |  | fid,flocaleid |
| 2 | pk_tcvat_rule_apportion_l |  | fpkid |

---

## 进项转出比例分摊台账-主表 t_tcvat_rule_apportion

- **表名称：** 进项转出比例分摊台账-主表
- **表名：** t_tcvat_rule_apportion

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisfromdraft11 | 取自收入明细底稿 | bpchar | 1 |  | √ | '0' | 取自收入明细底稿 |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fisfromdraft1 | 取自收入明细底稿 | bpchar | 1 |  | √ | '0' | 取自收入明细底稿 |
| 8 | fruletype | 规则类型 | varchar | 50 |  | √ | ' ' | 规则类型,枚举: private :自用规则 public :可分配规则 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fisfromdraft12 | 取自收入明细底稿 | bpchar | 1 |  | √ | '0' | 取自收入明细底稿 |
| 11 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fwfhfzclx | 无法划分转出类型 | varchar | 50 |  | √ | ' ' | 无法划分转出类型,枚举: 1 :免税项目 4 :简易计税方法计税项目 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | ftaxpayertype | 适用纳税人类型 | varchar | 50 |  | √ | ' ' | 适用纳税人类型,枚举: ybnsr :一般纳税人 xgmnsr :小规模纳税人 |
| 17 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tcvat_rule_apportion_1 |  | fnumber |
| 2 | pk_tcvat_rule_apportion |  | fid |

---

## 无法划分的全部进项税额-子表 t_tcvat_rule_apt_wfhf

- **表名称：** 无法划分的全部进项税额-子表
- **表名：** t_tcvat_rule_apt_wfhf

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffconditionjson | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 3 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | 数据源字段配置 tctb_datasource_entry |
| 4 | ftable | 数据源 | int8 | 64 |  | √ | 0 | 数据源配置 tctb_custom_datasource |
| 5 | fabsolute | 绝对值 | bpchar | 1 |  | √ | '0' | 绝对值 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fbizname | 业务名称 | varchar | 50 |  | √ | ' ' | 业务名称 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | ffiltercondition | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 10 | fdatadirection | 取数方向 | varchar | 50 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 11 | fdatatype | 取数方式 | varchar | 50 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 jsflqs :含税价换算不含税价 cysldsqs :税额换算不含税价 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvat_rule_apt_wfhf_fk |  | fid |
| 2 | pk_tcvat_rule_apt_wfhf |  | fentryid |
