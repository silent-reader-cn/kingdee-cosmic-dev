# 取数配置_财务报表-tcvvt_accessconfig

## 取数配置_财务报表-主表 t_tcvvt_accessconfig

- **表名称：** 取数配置_财务报表-主表
- **表名：** t_tcvvt_accessconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fruletype | 规则类型 | varchar | 50 |  | √ | ' ' | 规则类型,枚举: private :自用规则 public :可分配规则 |
| 7 | faccountstandard | 会计准则或制度 | int8 | 64 |  | √ | 0 | 会计准则业务定义分录 tpo_tccit_bizdef_kjzz |
| 8 | fapplicablerules | 适用取数规则 | int8 | 64 |  | √ | 0 | 自定义数据源适用取数规则 tctb_datasource_peek_rule |
| 9 | fdeclaretype | 申报类型 | varchar | 50 |  | √ | ',ansb,ayajsb,' | 申报类型,枚举: ansb :按年申报 ayajsb :按月/季申报 |
| 10 | fispreset | 系统预置 | bpchar | 1 |  | √ | ' ' | 系统预置 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | freporttype | 报表类型 | int8 | 64 |  | √ | 0 | 报表类型 tpo_reporttype |
| 16 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | faccessproject | 取数项目 | int8 | 64 |  | √ | 0 | 财务报表项目（树） tpo_bbbscwbb_tree |
| 18 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvvt_accessconfig |  | fid |
| 2 | idx_tcvvt_accessconfig |  | fnumber |

---

## 取数规则-子表 t_tcvvt_accessconf_entry

- **表名称：** 取数规则-子表
- **表名：** t_tcvvt_accessconf_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffconditionjson | 过滤条件 | varchar | 2000 |  | √ | ' ' | 过滤条件 |
| 3 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | 数据源字段配置 tctb_datasource_entry |
| 4 | fadvancedconfjson | 取数逻辑 | varchar | 2000 |  | √ | ' ' | 取数逻辑 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fbizname | 业务名称 | varchar | 200 |  | √ | ' ' | 业务名称 |
| 7 | ftable | 数据源 | int8 | 64 |  | √ | 0 | 数据源配置 tctb_custom_datasource |
| 8 | fabsolute | 绝对值 | bpchar | 1 |  | √ | '0' | 绝对值 |
| 9 | fadvancedconf | 取数逻辑 | varchar | 2000 |  | √ | ' ' | 取数逻辑 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | ffiltercondition | 过滤条件 | varchar | 2000 |  | √ | ' ' | 过滤条件 |
| 12 | fdatadirection | 取数方向 | varchar | 50 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 13 | fdatatype | 取数方式 | varchar | 50 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 jsflqs :价税分离取数 cysldsqs :除以税率倒算取数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvvt_accessconf_entry |  | fentryid |
| 2 | idx_tcvvt_accessconf_entry_fk |  | fid |

---

## 取数配置_财务报表-多语言表 t_tcvvt_accessconfig_l

- **表名称：** 取数配置_财务报表-多语言表
- **表名：** t_tcvvt_accessconfig_l

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
| 1 | pk_tcvvt_accessconfig_l |  | fpkid |
| 2 | idx_tcvvt_accessconfig_l_0 |  | fid,flocaleid |
