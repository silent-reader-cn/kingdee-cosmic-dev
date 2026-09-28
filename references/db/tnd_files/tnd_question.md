# 答疑澄清-tnd_question

## 供应商用户-多选基础资料表 t_src_supplieruser

- **表名称：** 供应商用户-多选基础资料表
- **表名：** t_src_supplieruser

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 供应商用户 pur_supuser |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_supplieruser_bid |  | fbasedataid |
| 2 | pk_src_supplieruser |  | fpkid |
| 3 | idx_src_supplieruser_fid |  | fid |

---

## 供应商范围-多选基础资料表 t_src_questionsupplier

- **表名称：** 供应商范围-多选基础资料表
- **表名：** t_src_questionsupplier

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_questionsupplier |  | fpkid |
| 2 | idx_src_questionsupplier_bid |  | fbasedataid |
| 3 | idx_src_questionsupplier_fid |  | fid |

---

## 答疑澄清-多语言表 t_src_question_l

- **表名称：** 答疑澄清-多语言表
- **表名：** t_src_question_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freplycontent | 回复内容 | varchar | 1000 |  | √ | ' ' | 回复内容 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fcontent | 发布内容 | varchar | 1000 |  | √ | ' ' | 发布内容 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_question_l |  | fpkid |
| 2 | idx_src_question_l_fid |  | fid,flocaleid |

---

## 答疑澄清-主表 t_src_question

- **表名称：** 答疑澄清-主表
- **表名：** t_src_question

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | freplycontent | freplycontent | varchar | 1000 |  | √ | ' ' |  |
| 3 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fpurdeptid | fpurdeptid | int8 | 64 |  | √ | 0 |  |
| 5 | fisclarify | 是否价格澄清 | bpchar | 1 |  | √ | '0' | 是否价格澄清 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fpublishtype | 发布类型 | bpchar | 1 |  | √ | ' ' | 发布类型,枚举: 1 :供应商提问 2 :采购方回复 3 :采购方澄清 4 :采购方提问 5 :供应商回复 6 :供应商澄清 7 :采购方价格澄清 |
| 8 | forigin | 发起方 | bpchar | 1 |  | √ | '1' | 发起方,枚举: 1 :采购方端 2 :供应商端 3 :两端公用 |
| 9 | fcreatorid | 发布人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fpackageid | 标段名称 | int8 | 64 |  | √ | 0 | 标段名称 src_packagef7 |
| 11 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 12 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fresponderid | 回复人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fprojectid | 招标项目名称 | int8 | 64 |  | √ | 0 | 招标项目F7 src_projectf7 |
| 15 | fbillstatus | 发布状态 | bpchar | 1 |  | √ | ' ' | 发布状态,枚举: A :暂存 B :已提交 C :已发布 |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | fsrcbillid | 回复的源单ID | int8 | 64 |  | √ | 0 | 回复的源单ID |
| 18 | freplytime | 回复时间 | timestamp | 0 |  |  | null | 回复时间 |
| 19 | fauditdate | 发布时间 | timestamp | 0 |  |  | null | 发布时间 |
| 20 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | 商务伙伴 bd_bizpartner |
| 21 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 注册供应商 src_supplier |
| 22 | fduedate | 答疑截止时间 | timestamp | 0 |  |  | null | 答疑截止时间 |
| 23 | fsuppliertype | 供应商类别 | varchar | 30 |  | √ | ' ' | 供应商类别,枚举: src_supplier :注册供应商 src_supplier_inner :内部供应商(员工) src_supplier_tmp :临时供应商 bd_supplier :供应商 |
| 24 | fquestype | 问题类型 | bpchar | 1 |  | √ | ' ' | 问题类型,枚举: 1 :技术 2 :商务 3 :商务综合 4 :资质预审 7 :资质后审 |
| 25 | fisprice | fisprice | bpchar | 1 |  | √ | '1' |  |
| 26 | fcontent | fcontent | varchar | 1000 |  | √ | ' ' |  |
| 27 | fcurrentnode | 当前节点 | int8 | 64 |  | √ | 0 | 业务节点 pds_biznode |
| 28 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_question_createtime |  | fcreatetime |
| 2 | pk_src_question |  | fid |
| 3 | idx_src_question_project |  | fprojectid |
| 4 | idx_src_question_billno |  | fbillno |
| 5 | idx_src_question_publishtype |  | fpublishtype |
| 6 | idx_src_question_package |  | fpackageid |
| 7 | idx_src_question_supplier |  | fsupplierid |

---

## 价格澄清分录-子表 t_src_priceclarify

- **表名称：** 价格澄清分录-子表
- **表名：** t_src_priceclarify

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpricenew | 未税单价(澄清后) | numeric | 23 | 10 | √ | 0 | 未税单价(澄清后) |
| 3 | fsrcentryid | 源单分录ID | varchar | 50 |  | √ | ' ' | 源单分录ID |
| 4 | ftaxrate | 税率(%)(澄清前) | numeric | 23 | 10 | √ | 0 | 税率(%)(澄清前) |
| 5 | fmaterialid | 标的编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 6 | fentrystatus | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: A :待报价 B :已报价 C :已开标 D :已关闭 E :已定标 F :已签约 G :暂存 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fnote | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 9 | ftaxprice | 含税单价(澄清前) | numeric | 23 | 10 | √ | 0 | 含税单价(澄清前) |
| 10 | famount | 未税金额(澄清前) | numeric | 23 | 10 | √ | 0 | 未税金额(澄清前) |
| 11 | fprice | 未税单价(澄清前) | numeric | 23 | 10 | √ | 0 | 未税单价(澄清前) |
| 12 | fcurrencyidnew | 报价币别(澄清后) | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 13 | fmaterialnane | 标的名称 | varchar | 100 |  | √ | ' ' | 标的名称 |
| 14 | ftaxpricenew | 含税单价(澄清后) | numeric | 23 | 10 | √ | 0 | 含税单价(澄清后) |
| 15 | fturns | 轮次 | varchar | 2 |  | √ | ' ' | 轮次,枚举: 1 :首轮 2 :议价(1) 3 :议价(2) 4 :议价(3) 5 :议价(4) 6 :议价(5) |
| 16 | fcategoryid | 品类 | int8 | 64 |  | √ | 0 | 物料分类 bd_materialgroup |
| 17 | fisnew | 是否澄清 | bpchar | 1 |  | √ | '0' | 是否澄清 |
| 18 | ftaxratenew | 税率(%)(澄清后) | numeric | 23 | 10 | √ | 0 | 税率(%)(澄清后) |
| 19 | fispresentnew | 赠品(澄清后) | bpchar | 1 |  | √ | '0' | 赠品(澄清后) |
| 20 | fmaterialmodel | 规格型号 | varchar | 1024 |  | √ | ' ' | 规格型号 |
| 21 | ftaxamount | 价税合计(澄清前) | numeric | 23 | 10 | √ | 0 | 价税合计(澄清前) |
| 22 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 23 | ftaxitemidnew | 税率(澄清后) | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 24 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 25 | fispresent | 赠品(澄清前) | bpchar | 1 |  | √ | '0' | 赠品(澄清前) |
| 26 | fpackagename | 标段 | varchar | 50 |  | √ | ' ' | 标段 |
| 27 | fdescription | 物料描述 | varchar | 1024 |  | √ | ' ' | 物料描述 |
| 28 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 29 | ftaxitemid | 税率(澄清前) | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 30 | fisdiscardednew | 弃标的(澄清后) | bpchar | 1 |  | √ | '0' | 弃标的(澄清后) |
| 31 | famountnew | 未税金额(澄清后) | numeric | 23 | 10 | √ | 0 | 未税金额(澄清后) |
| 32 | ftaxamountnew | 价税合计(澄清后) | numeric | 23 | 10 | √ | 0 | 价税合计(澄清后) |
| 33 | fqtynew | 数量(澄清后) | numeric | 23 | 10 | √ | 0 | 数量(澄清后) |
| 34 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 35 | fcurrencyid | 报价币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 36 | fisdiscarded | 弃标的(澄清前) | bpchar | 1 |  | √ | '0' | 弃标的(澄清前) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_priceclarify |  | fentryid |
| 2 | idx_src_priceclarify_fid |  | fid |
