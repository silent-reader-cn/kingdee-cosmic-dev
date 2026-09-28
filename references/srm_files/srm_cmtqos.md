# 企业质量保障能力-srm_cmtqos

## 主要检验设备情况分录-子表 t_srm_compinspect

- **表名称：** 主要检验设备情况分录-子表
- **表名：** t_srm_compinspect

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finspectdate | 校准有效期 | timestamp | 0 |  |  | null | 校准有效期 |
| 3 | fequipmentname | 检测设备名称 | varchar | 255 |  | √ | ' ' | 检测设备名称 |
| 4 | fprojectnum | 数量 | int8 | 64 |  | √ | 0 | 数量 |
| 5 | fbuydate | 购入日期 | timestamp | 0 |  |  | null | 购入日期 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | faccuracy | 精度 | varchar | 100 |  | √ | ' ' | 精度 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | finspectproject | 可检测项目 | varchar | 255 |  | √ | ' ' | 可检测项目 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_srm_compinspect_fid |  | fid |
| 2 | pk_t_srm_compinspect |  | fentryid |

---

## 附件-附件表 t_srm_compqosaptitude_fj

- **表名称：** 附件-附件表
- **表名：** t_srm_compqosaptitude_fj

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 附件字段实体 bd_attachment |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_compqosaptitude_fj |  | fentryid |
| 2 | pk_t_srm_compqosaptitude_fj |  | fpkid |

---

## 企业质量保障能力-主表 t_srm_compentqos

- **表名称：** 企业质量保障能力-主表
- **表名：** t_srm_compentqos

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fprojectid | 寻源项目F7 | int8 | 64 |  | √ | 0 | 招标项目F7 src_projectf7 |
| 3 | fparentid | 父单据ID | varchar | 100 |  | √ | ' ' | 父单据ID |
| 4 | fentitykey | 组件标识 | varchar | 100 |  | √ | ' ' | 组件标识 |
| 5 | fmainorgid | 主业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fpentitykey | 父单据标识 | varchar | 100 |  | √ | ' ' | 父单据标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_srm_compentqos |  | fid |
| 2 | idx_srm_compentqos_parent |  | fparentid |

---

## 资质信息分录-子表 t_srm_compqosaptitude

- **表名称：** 资质信息分录-子表
- **表名：** t_srm_compqosaptitude

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdateto | 有效日期至 | timestamp | 0 |  |  | null | 有效日期至 |
| 3 | faptitudename | 资质名称 | varchar | 255 |  | √ | ' ' | 资质名称 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 6 | fissuedate | 签发日期 | timestamp | 0 |  |  | null | 签发日期 |
| 7 | fcompanytypeid | 供货类型 | int8 | 64 |  | √ | 0 | 供货类型 bd_company_type |
| 8 | frequired | 必选 | bpchar | 1 |  | √ | '0' | 必选 |
| 9 | faptitudenumber | 资质编号 | varchar | 100 |  | √ | ' ' | 资质编号 |
| 10 | ftype | 资质类型 | varchar | 10 |  | √ | ' ' | 资质类型,枚举: 1 :三/五证合一 2 :营业执照 3 :税务登记证 4 :组织机构代码证 5 :社会保险登记证 6 :一般纳税人证明材料 7 :统计登记证 8 :其他证照 |
| 11 | fissueorg | 签发机构 | varchar | 255 |  | √ | ' ' | 签发机构 |
| 12 | faptitudetypeid | 资质类型-新 | int8 | 64 |  | √ | 0 | 资质类型维护 bd_qualification_type |
| 13 | fcheckdate | 最近年检时间 | timestamp | 0 |  |  | null | 最近年检时间 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 15 | fgrade | 资质等级 | varchar | 100 |  | √ | ' ' | 资质等级 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_srm_cpqosaptitude_fid |  | fid |
| 2 | pk_t_srm_compqosaptitude |  | fentryid |
