# 企业基本信息-srm_cmtbase

## 企业基本信息-多语言表 t_srm_compentbase_l

- **表名称：** 企业基本信息-多语言表
- **表名：** t_srm_compentbase_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 供应商名称 | varchar | 255 |  | √ | ' ' | 供应商名称 |
| 3 | faddress | 联系地址 | varchar | 255 |  | √ | ' ' | 联系地址 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fartificialperson | 法人代表 | varchar | 255 |  | √ | ' ' | 法人代表 |
| 6 | fpkid | fpkid | varchar | 40 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_srm_compentbase_l |  | fpkid |
| 2 | idx_srm_cptbase_l_fid |  | fid |

---

## 银行信息-子表 t_srm_compbasebank

- **表名称：** 银行信息-子表
- **表名：** t_srm_compbasebank

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbanknote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | faccountname | 账户名称 | varchar | 255 |  | √ | ' ' | 账户名称 |
| 4 | faccounttype | 账户类型 | varchar | 10 |  | √ | ' ' | 账户类型,枚举: 1 :基本账户 2 :请款账户 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | faccount | 银行账号 | varchar | 100 |  | √ | ' ' | 银行账号 |
| 7 | fbankid | 开户银行 | int8 | 64 |  | √ | 0 | [行名行号 bd_bebank](../basedata_files/bd_bebank.md) |
| 8 | facccurrid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fisdefault | 默认 | bpchar | 1 |  | √ | '0' | 默认 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_srm_compbasebank |  | fentryid |
| 2 | idx_srm_compbaseban_fid |  | fid |

---

## 联系人信息-子表 t_srm_compbaselink

- **表名称：** 联系人信息-子表
- **表名：** t_srm_compbaselink

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fphone | 电话 | varchar | 50 |  | √ | ' ' | 电话 |
| 3 | femail | 邮箱 | varchar | 100 |  | √ | ' ' | 邮箱 |
| 4 | fgender | 性别 | varchar | 5 |  | √ | ' ' | 性别,枚举: 1 :男 2 :女 |
| 5 | fdept | 部门 | varchar | 100 |  | √ | ' ' | 部门 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fbizscopetype | 负责业务 | varchar | 5 |  | √ | ' ' | 负责业务,枚举: A :业务 B :财务 C :PO接收 D :其他 |
| 8 | fmobile | 手机号 | varchar | 50 |  | √ | ' ' | 手机号 |
| 9 | fduty | 职务 | varchar | 100 |  | √ | ' ' | 职务 |
| 10 | fisdefault_link | 默认 | bpchar | 1 |  | √ | '0' | 默认 |
| 11 | flinkname | 姓名 | varchar | 255 |  | √ | ' ' | 姓名 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fbizscope | 备注 | varchar | 255 |  | √ | ' ' | 备注 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_srm_cbaselink_fid |  | fid |
| 2 | pk_t_srm_compbaselink |  | fentryid |

---

## 企业基本信息-主表 t_srm_compentbase

- **表名称：** 企业基本信息-主表
- **表名：** t_srm_compentbase

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 供应商名称 | varchar | 255 |  | √ | ' ' | 供应商名称 |
| 3 | faddress | 联系地址 | varchar | 255 |  | √ | ' ' | 联系地址 |
| 4 | fdatachannel | 信息获取渠道 | varchar | 255 |  | √ | ' ' | 信息获取渠道 |
| 5 | finvoicetypeid | 发票类型 | int8 | 64 |  | √ | 0 | [发票种类 bd_invoicetype](../basedata_files/bd_invoicetype.md) |
| 6 | fprojectid | 寻源项目F7 | int8 | 64 |  | √ | 0 | [招标项目F7 src_projectf7](../src_files/src_projectf7.md) |
| 7 | fparentid | 父单据ID | varchar | 100 |  | √ | ' ' | 父单据ID |
| 8 | fsocietycreditcode | 统一社会信用代码 | varchar | 255 |  | √ | ' ' | 统一社会信用代码 |
| 9 | ftaxclass | 纳税人类型 | varchar | 10 |  | √ | ' ' | 纳税人类型,枚举: 1 :一般纳税人 2 :小规模纳税人 3 :非增值税纳税人 |
| 10 | fentitykey | 组件标识 | varchar | 100 |  | √ | ' ' | 组件标识 |
| 11 | fmainorgid | 主业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 12 | fregcapital | 注册资本 | numeric | 23 | 10 | √ | 0 | 注册资本 |
| 13 | fpentitykey | 父单据标识 | varchar | 100 |  | √ | ' ' | 父单据标识 |
| 14 | fregdate | 企业成立日期 | timestamp | 0 |  |  | null | 企业成立日期 |
| 15 | ftelephone | 企业电话 | varchar | 100 |  | √ | ' ' | 企业电话 |
| 16 | ftype | 企业类型 | varchar | 10 |  | √ | ' ' | 企业类型,枚举: 1 :法人企业 2 :国家机关 3 :事业单位 4 :社会团体 5 :其他组织机构 6 :个体户 7 :个人 8 :非法人企业 |
| 17 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 18 | furl | 企业网址 | varchar | 255 |  | √ | ' ' | 企业网址 |
| 19 | fartificialperson | 法人代表 | varchar | 255 |  | √ | ' ' | 法人代表 |
| 20 | ftxregisterno | 纳税人识别号 | varchar | 255 |  | √ | ' ' | 纳税人识别号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_srm_compentbase |  | fid |
| 2 | idx_srm_cptbase_parentid |  | fparentid |
