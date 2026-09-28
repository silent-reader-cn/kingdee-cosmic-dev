# 取数配置_重点税源-tcvvt_tax_accessconfig

## 取数配置_重点税源-主表 t_tcvvt_tax_accessconfig

- **表名称：** 取数配置_重点税源-主表
- **表名：** t_tcvvt_tax_accessconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fruletype | 规则类型 | varchar | 50 |  | √ | ' ' | 规则类型,枚举: private :自用规则 public :可分配规则 |
| 7 | fapplicablerules | 适用取数规则 | int8 | 64 |  | √ | 0 | 自定义数据源适用取数规则 tctb_datasource_peek_rule |
| 8 | fispreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | freporttype | 报表类型 | varchar | 50 |  | √ | ' ' | 报表类型,枚举: tax :税收表 finance :财务表 qyjqdcb :企业景气调查表 |
| 14 | faccessproject | 取数项目 | int8 | 64 |  | √ | 0 | 重点税源报表项目 tpo_keytaxsrc |
| 15 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvvt_tax_accessconfig |  | fid |
| 2 | idx_tcvvt_taxaccess_org |  | forgid,faccessproject |

---

## 取数配置_重点税源-多语言表 t_tcvvt_tax_accessconfig_l

- **表名称：** 取数配置_重点税源-多语言表
- **表名：** t_tcvvt_tax_accessconfig_l

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
| 1 | pk_tcvvt_tax_accessconfig_l |  | fpkid |
| 2 | idx_tcvvt_tax_accessconfig_l_0 |  | fid,flocaleid |

---

## 取数规则-子表 t_tcvvt_taxaccess_entry

- **表名称：** 取数规则-子表
- **表名：** t_tcvvt_taxaccess_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffconditionjson | 过滤条件 | varchar | 2000 |  | √ | ' ' | 过滤条件 |
| 3 | fexratejson | 汇率转换 | varchar | 256 |  | √ | ' ' | 汇率转换 |
| 4 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | 数据源字段配置 tctb_datasource_entry |
| 5 | fadvancedconfjson | 取数逻辑 | varchar | 2000 |  | √ | ' ' | 取数逻辑 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fbizname | 业务名称 | varchar | 50 |  | √ | ' ' | 业务名称 |
| 8 | ftable | 数据源 | int8 | 64 |  | √ | 0 | 数据源配置 tctb_custom_datasource |
| 9 | fvatrate | 增值税税率 | numeric | 23 | 2 | √ | 0 | 增值税税率 |
| 10 | fjsbl | 系数 | numeric | 23 | 10 | √ | 0 | 系数 |
| 11 | fabsolute | 绝对值 | bpchar | 1 |  | √ | '0' | 绝对值 |
| 12 | fadvancedconf | 取数逻辑 | varchar | 2000 |  | √ | ' ' | 取数逻辑 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | ffiltercondition | 过滤条件 | varchar | 2000 |  | √ | ' ' | 过滤条件 |
| 15 | fdatadirection | 取数方向 | varchar | 50 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 16 | fdatatype | 取数方式 | varchar | 50 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 jsflqs :含税价换算不含税价 cysldsqs :税额换算不含税价 sehshsj :税额换算含税价 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvvt_taxaccess_entry_fk |  | fid |
| 2 | pk_tcvvt_taxaccess_entry |  | fentryid |
