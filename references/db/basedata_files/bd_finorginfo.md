# 金融机构-bd_finorginfo

## 关联子实体-子表 t_bd_finorginfo_lk

- **表名称：** 关联子实体-子表
- **表名：** t_bd_finorginfo_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_finorginfo_lk_fk |  | fid |
| 2 | pk_bd_finorginfo_lk |  | fpkid |

---

## 金融机构-多语言表 t_bd_finorginfo_l

- **表名称：** 金融机构-多语言表
- **表名：** t_bd_finorginfo_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 500 |  |  | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bd_finorginfo_l_fid |  | fid,flocaleid,fname |
| 2 | idx_bd_finorginfo_l_fid |  | fid |
| 3 | pk_t_bd_finorginfo_l |  | fpkid |

---

## 金融机构-主表 t_bd_finorginfo

- **表名称：** 金融机构-主表
- **表名：** t_bd_finorginfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faddress | 地址 | varchar | 255 |  | √ | ' ' | 地址 |
| 3 | flogo | LOGO | varchar | 255 |  | √ | ' ' | LOGO |
| 4 | fisleaf | 是否叶节点 | bpchar | 1 |  | √ | '0' | 是否叶节点 |
| 5 | froutingnum | Routing Number | varchar | 100 |  | √ | ' ' | Routing Number |
| 6 | fcityid | 城市 | int8 | 64 |  | √ | 0 | [行政区划 bd_admindivision](../base_files/bd_admindivision.md) |
| 7 | forgid | 对应业务单元 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | ffinorgtypeid | 金融机构类别 | int8 | 64 |  | √ | 0 | [金融机构类别 bd_finorgtype](../basedata_files/bd_finorgtype.md) |
| 9 | fdisabletime | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fbankcateresid | 行名行号 | int8 | 64 |  | √ | 0 | [行名行号 bd_bebank](../basedata_files/bd_bebank.md) |
| 13 | fsourdata | 数据来源 | varchar | 80 |  | √ | ' ' | 数据来源,枚举: YWDY :业务单元 |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fprovinceid | 省份 | int8 | 64 |  | √ | 0 | [行政区划 bd_admindivision](../base_files/bd_admindivision.md) |
| 17 | fcontactman | 联系人 | varchar | 50 |  | √ | ' ' | 联系人 |
| 18 | fnameeng | 名称（英文） | varchar | 255 |  | √ | ' ' | 名称（英文） |
| 19 | ffax | 传真 | varchar | 50 |  | √ | ' ' | 传真 |
| 20 | fothercode | 其他代码 | varchar | 50 |  | √ | ' ' | 其他代码 |
| 21 | faddresseng | 地址（英文） | varchar | 255 |  | √ | ' ' | 地址（英文） |
| 22 | fswiftcode | SWIFT Code | varchar | 50 |  | √ | ' ' | SWIFT Code |
| 23 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fname | 名称 | varchar | 500 |  |  | ' ' | 名称 |
| 25 | fiban | fiban | varchar | 100 |  | √ | ' ' |  |
| 26 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 27 | fparentid | 上级机构 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 28 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 29 | forgnumber | 金融许可证机构编码 | varchar | 50 |  | √ | ' ' | 金融许可证机构编码 |
| 30 | flongnumber | 长编码 | varchar | 80 |  | √ | ' ' | 长编码 |
| 31 | fcountryid | 国家地区 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 32 | fbankcateid | 银行类别 | int8 | 64 |  | √ | 0 | [银行类别 bd_bankcgsetting](../basedata_files/bd_bankcgsetting.md) |
| 33 | ftelephone | 电话 | varchar | 50 |  | √ | ' ' | 电话 |
| 34 | fenabletime | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 35 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 36 | fnameloc | fnameloc | varchar | 50 |  | √ | ' ' |  |
| 37 | fsimplename | 简称 | varchar | 50 |  | √ | ' ' | 简称 |
| 38 | funioncode | 联行号 | varchar | 50 |  | √ | ' ' | 联行号 |
| 39 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 40 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_finorginfo_num |  | fnumber |
| 2 | pk_t_bd_finorginfo |  | fid |
