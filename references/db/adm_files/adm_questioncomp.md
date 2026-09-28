# 填写调查问卷-adm_questioncomp

## 填写调查问卷-主表 t_srm_questioncomp

- **表名称：** 填写调查问卷-主表
- **表名：** t_srm_questioncomp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 调查问卷名称 | varchar | 100 |  | √ | ' ' | 调查问卷名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | ftemplateid | 模板 | int8 | 64 |  | √ | 0 | 组件模板配置 pds_tplconfig |
| 5 | fbillstatus | 处理状态 | varchar | 5 |  | √ | ' ' | 处理状态,枚举: A :未处理 B :已提交 C :已审核 |
| 6 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | forgid | 发布组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | flockstatus | 锁定状态 | varchar | 5 |  | √ | ' ' | 锁定状态,枚举: A :未锁定 B :已锁定 |
| 10 | freleasedate | freleasedate | timestamp | 0 |  |  | null |  |
| 11 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 13 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | 商务伙伴 bd_bizpartner |
| 14 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 srm_supplier |
| 15 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 17 | fquestionbillno | 问卷编码 | varchar | 80 |  | √ | ' ' | 问卷编码 |
| 18 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fsrcsupquestionid | 供应商调查问卷详情ID | varchar | 50 |  | √ | ' ' | 供应商调查问卷详情ID |
| 20 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 21 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_srm_questioncomp |  | fid |
| 2 | idx_srm_questioncomp_biz |  | fbizpartnerid |
| 3 | idx_srm_questioncomp_sup |  | fsupplierid |

---

## 模板分录-子表 t_srm_projecttpl

- **表名称：** 模板分录-子表
- **表名：** t_srm_projecttpl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomponentid | 业务组件 | int8 | 64 |  | √ | 0 | 组件注册 pds_compreg |
| 3 | ftemplateid | 组件模板 | int8 | 64 |  | √ | 0 | 组件模板配置 pds_tplconfig |
| 4 | fbizobject | 业务对象 | varchar | 100 |  | √ | ' ' | 业务对象 |
| 5 | fsrctplid | 来源模板ID | varchar | 100 |  | √ | ' ' | 来源模板ID |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_srm_projecttpl |  | fentryid |
| 2 | idx_t_srm_projecttpl |  | fid |

---

## 填写调查问卷-多语言表 t_srm_questioncomp_l

- **表名称：** 填写调查问卷-多语言表
- **表名：** t_srm_questioncomp_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 调查问卷名称 | varchar | 100 |  | √ | ' ' | 调查问卷名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_srm_questioncomp_l |  | fpkid |
| 2 | idx_srm_questioncomp_l_fid |  | fid |
