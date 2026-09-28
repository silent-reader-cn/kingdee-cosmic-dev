# 行名行号-bd_bebank

## 行名行号-多语言表 t_bd_bebank_l

- **表名称：** 行名行号-多语言表
- **表名：** t_bd_bebank_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  |  | null |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | faddress | faddress | varchar | 255 |  |  | null |  |
| 4 | flocaleid | flocaleid | varchar | 10 |  |  | null | localeid |
| 5 | fdescription | fdescription | varchar | 255 |  |  | null |  |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bd_bebank_l_fname |  | fname,flocaleid |
| 2 | idx_t_bd_bebank_l_name |  | fname |
| 3 | t_bd_bebank_l_pkey |  | fpkid |
| 4 | idx_t_bd_bebank_id |  | fid,flocaleid |

---

## 行名行号-主表 t_bd_bebank

- **表名称：** 行名行号-主表
- **表名：** t_bd_bebank

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fmodifyorgid | fmodifyorgid | int8 | 64 |  |  | null |  |
| 3 | faddress | 地址 | varchar | 255 |  | √ | ' ' | 地址 |
| 4 | froutingnum | Routing Number | varchar | 100 |  | √ | ' ' | Routing Number |
| 5 | fcityid | 城市 | int8 | 64 |  | √ | 0 | [行政区划 bd_admindivision](../base_files/bd_admindivision.md) |
| 6 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 7 | fmunicipality | fmunicipality | varchar | 100 |  |  | null |  |
| 8 | fcitycloud | 城市(云端) | varchar | 255 |  | √ | ' ' | 城市(云端) |
| 9 | fcounty | fcounty | varchar | 100 |  |  | null |  |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | varchar | 50 |  |  | null | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 14 | fprovinceid | 省份 | int8 | 64 |  | √ | 0 | [行政区划 bd_admindivision](../base_files/bd_admindivision.md) |
| 15 | fissystem | fissystem | bpchar | 1 |  |  | null |  |
| 16 | fnameeng | 名称英文 | varchar | 255 |  | √ | ' ' | 名称英文 |
| 17 | ffax | 传真 | varchar | 50 |  | √ | ' ' | 传真 |
| 18 | fothercode | 其他代码 | varchar | 100 |  | √ | ' ' | 其他代码 |
| 19 | fprovincetxt | 省份（银企） | varchar | 255 |  | √ | ' ' | 省份（银企） |
| 20 | faddresseng | 地址(英文) | varchar | 255 |  | √ | ' ' | 地址(英文) |
| 21 | fswiftcode | SWIFT Code | varchar | 50 |  | √ | ' ' | SWIFT Code |
| 22 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 23 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 25 | fiban | fiban | varchar | 100 |  | √ | ' ' |  |
| 26 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 27 | ffintypeid | ffintypeid | int8 | 64 |  | √ | 0 |  |
| 28 | fcountryid | 国家地区 | int8 | 64 |  |  | null | [国家和地区 bd_country](../base_files/bd_country.md) |
| 29 | fbankcategory | fbankcategory | varchar | 50 |  | √ | ' ' |  |
| 30 | fdisablerid | 禁用人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 31 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 32 | fisfromcloud | 云端数据 | bpchar | 1 |  | √ | '0' | 云端数据 |
| 33 | ftelephone | 电话 | varchar | 50 |  | √ | ' ' | 电话 |
| 34 | fendlifecycle | 过期操作日期 | timestamp | 0 |  |  | null | 过期操作日期 |
| 35 | fbankcateid | 银行类别 | int8 | 64 |  | √ | 0 | [银行类别 bd_bankcgsetting](../basedata_files/bd_bankcgsetting.md) |
| 36 | fbankcatename | 银行类别名称 | varchar | 255 |  | √ | ' ' | 银行类别名称 |
| 37 | fonlineupdatetime | 在线更新日期 | timestamp | 0 |  |  | null | 在线更新日期 |
| 38 | fadmindivisionid | fadmindivisionid | int8 | 64 |  |  | null |  |
| 39 | fprovincecloud | 省份(云端) | varchar | 255 |  | √ | ' ' | 省份(云端) |
| 40 | fbanktypecode | 行别代码 | varchar | 100 |  | √ | ' ' | 行别代码 |
| 41 | funioncode | 联行号 | varchar | 50 |  | √ | ' ' | 联行号 |
| 42 | fcitytxt | 城市（银企） | varchar | 255 |  | √ | ' ' | 城市（银企） |
| 43 | fenable | 使用状态 | bpchar | 1 |  |  | null | 使用状态,枚举: 0 :禁用 1 :可用 |
| 44 | fbankcateg | fbankcateg | varchar | 100 |  |  | null |  |
| 45 | fnumber | 编码 | varchar | 80 |  |  | null | 编码 |
| 46 | fprovince | fprovince | varchar | 100 |  |  | null |  |
| 47 | fisoverdue | 疑似过期 | bpchar | 1 |  | √ | 'N' | 疑似过期,枚举: Y :是 N :否 |
| 48 | fnamezhc | 名称中文 | varchar | 500 |  | √ | ' ' | 名称中文 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bd_bebank_fname |  | fname |
| 2 | idx_t_bd_bebank_number |  | fnumber |
| 3 | idx_t_bd_bebank_fcityid |  | fcityid |
| 4 | idx_t_bd_bebank_fcountryid |  | fcountryid |
| 5 | idx_t_bd_bebank_fnameeng |  | fnameeng |
| 6 | pk_t_bd_bebank |  | fid |
| 7 | idx_t_bd_bebank_fisfromcloud |  | fisfromcloud |
| 8 | idx_t_bd_bebank_fprovinceid |  | fprovinceid |
