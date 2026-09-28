# 我要澄清-src_clarify

## 我要澄清-多语言表 t_src_question_l

- **表名称：** 我要澄清-多语言表
- **表名：** t_src_question_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freplycontent | freplycontent | varchar | 1000 |  | √ | ' ' |  |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fcontent | 澄清内容 | varchar | 1000 |  | √ | ' ' | 澄清内容 |
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

## 我要澄清-主表 t_src_question

- **表名称：** 我要澄清-主表
- **表名：** t_src_question

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | freplycontent | freplycontent | varchar | 1000 |  | √ | ' ' |  |
| 3 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fpurdeptid | 采购部门 | int8 | 64 |  | √ | 0 | 采购部门 pds_purdepart |
| 5 | fisclarify | 是否价格澄清 | bpchar | 1 |  | √ | '0' | 是否价格澄清 |
| 6 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 7 | fpublishtype | 发布类型 | bpchar | 1 |  | √ | ' ' | 发布类型,枚举: 1 :供应商提问 2 :采购方回复 3 :采购方澄清 4 :采购方提问 5 :供应商回复 6 :供应商澄清 |
| 8 | forigin | 发起方 | bpchar | 1 |  | √ | '1' | 发起方,枚举: 1 :采购方端 2 :供应商端 3 :两端公用 |
| 9 | fcreatorid | 发布人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fpackageid | 标段名称 | int8 | 64 |  | √ | 0 | 标段名称 src_packagef7 |
| 11 | fbillno | 澄清编号 | varchar | 30 |  | √ | ' ' | 澄清编号 |
| 12 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 13 | fresponderid | fresponderid | int8 | 64 |  | √ | 0 |  |
| 14 | fprojectid | 招标项目 | int8 | 64 |  | √ | 0 | 招标项目F7 src_projectf7 |
| 15 | fbillstatus | 业务状态 | bpchar | 1 |  | √ | ' ' | 业务状态,枚举: A :未回复 B :已回复 |
| 16 | fcreatetime | 澄清时间 | timestamp | 0 |  |  | null | 澄清时间 |
| 17 | fsrcbillid | fsrcbillid | int8 | 64 |  | √ | 0 |  |
| 18 | freplytime | freplytime | timestamp | 0 |  |  | null |  |
| 19 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
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
