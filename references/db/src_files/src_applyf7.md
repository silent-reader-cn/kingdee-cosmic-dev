# 寻源申请F7-src_applyf7

## 寻源申请F7-多语言表 t_src_apply_l

- **表名称：** 寻源申请F7-多语言表
- **表名：** t_src_apply_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftitle | 申请名称 | varchar | 300 |  | √ | ' ' | 申请名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_apply_l |  | fpkid |
| 2 | idx_src_apply_l_flocaleid |  | fid,flocaleid |

---

## 寻源申请F7-主表 t_src_apply

- **表名称：** 寻源申请F7-主表
- **表名：** t_src_apply

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 2 | freqdatetime | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 3 | fdemandaffiliateid | fdemandaffiliateid | int8 | 64 |  | √ | 0 |  |
| 4 | fisproject | 下推类型 | bpchar | 1 |  | √ | '0' | 下推类型,枚举: 0 :手工下推项目立项 1 :手工下推项目启动 2 :审核自动下推项目启动 |
| 5 | forgid | 需求组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fspecialreason | fspecialreason | varchar | 300 |  |  | ' ' |  |
| 7 | famount | famount | numeric | 23 | 10 | √ | 0 |  |
| 8 | fsrctypeid | 寻源流程 | int8 | 64 |  | √ | 0 | [流程配置 pds_flowconfig](../pds_files/pds_flowconfig.md) |
| 9 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 10 | freqsource | freqsource | varchar | 30 |  | √ | ' ' |  |
| 11 | ftitle | ftitle | varchar | 300 |  | √ | ' ' |  |
| 12 | fattachurl | fattachurl | varchar | 500 |  | √ | ' ' |  |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fsuppliernoid | fsuppliernoid | int8 | 64 |  | √ | 0 |  |
| 15 | fsumamount | 预估未税金额 | numeric | 23 | 10 | √ | 0 | 预估未税金额 |
| 16 | fisdecision | fisdecision | bpchar | 1 |  | √ | '0' |  |
| 17 | freqclass | freqclass | varchar | 3 |  | √ | 'A' |  |
| 18 | fprojectno | fprojectno | varchar | 100 |  | √ | ' ' |  |
| 19 | frentsupplierid | frentsupplierid | int8 | 64 |  | √ | 0 |  |
| 20 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 21 | ftaxtype | 价格录入方式 | bpchar | 1 |  | √ | '1' | 价格录入方式,枚举: 1 :录入含税价 2 :录入未税价 3 :价内税(含税) |
| 22 | fbillno | 申请编号 | varchar | 60 |  | √ | ' ' | 申请编号 |
| 23 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 24 | fecpno | fecpno | varchar | 100 |  | √ | ' ' |  |
| 25 | fserviceattributes | fserviceattributes | varchar | 50 |  | √ | ' ' |  |
| 26 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 D :已作废 |
| 27 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 28 | fsuppliernametext | fsuppliernametext | varchar | 50 |  | √ | ' ' |  |
| 29 | fcostattribution | fcostattribution | int8 | 64 |  | √ | 0 |  |
| 30 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 31 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 32 | fisspecial | fisspecial | bpchar | 1 |  | √ | '0' |  |
| 33 | fdepartmentid | fdepartmentid | int8 | 64 |  | √ | 0 |  |
| 34 | fsumqty | fsumqty | numeric | 23 | 10 | √ | 0 |  |
| 35 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 36 | fyearcomment | fyearcomment | varchar | 255 |  | √ | ' ' |  |
| 37 | forigncreator | forigncreator | int8 | 64 |  | √ | 0 |  |
| 38 | ftype | ftype | varchar | 30 |  | √ | ' ' |  |
| 39 | fbasedatafield | fbasedatafield | int8 | 64 |  | √ | 0 |  |
| 40 | fsourcetypeid | fsourcetypeid | int8 | 64 |  | √ | 0 |  |
| 41 | fsumtaxamount | 预估价税合计 | numeric | 23 | 10 | √ | 0 | 预估价税合计 |
| 42 | fsumtax | fsumtax | numeric | 23 | 10 | √ | 0 |  |
| 43 | fisannual | fisannual | varchar | 30 |  | √ | '0' |  |
| 44 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 45 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 46 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_apply_fecpno |  | fecpno |
| 2 | idx_src_apply_fbillno |  | fbillno |
| 3 | pk_src_apply |  | fid |
