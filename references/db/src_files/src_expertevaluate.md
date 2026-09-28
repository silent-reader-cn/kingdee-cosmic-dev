# 专家考评-src_expertevaluate

## 模板分录-子表 t_src_evaluatetpl

- **表名称：** 模板分录-子表
- **表名：** t_src_evaluatetpl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomponentid | 业务组件 | int8 | 64 |  | √ | 0 | 组件注册 pds_compreg |
| 3 | ftemplateid | 组件模板 | int8 | 64 |  | √ | 0 | 组件模板配置 pds_tplconfig |
| 4 | fbizobject | 业务对象 | varchar | 50 |  | √ | ' ' | 业务对象 |
| 5 | fsrctplid | 来源模板ID | varchar | 50 |  | √ | ' ' | 来源模板ID |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_evaluatetpl |  | fentryid |
| 2 | idx_src_evaluatetpl_id |  | fid |

---

## 专家考评-主表 t_src_evaluate

- **表名称：** 专家考评-主表
- **表名：** t_src_evaluate

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 发起组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fbizstatus | 业务状态 | bpchar | 1 |  | √ | ' ' | 业务状态,枚举: A :未开始 B :处理中 C :已处理 D :已终止/流标 E :已废标 Z :无需处理 |
| 4 | fisevaluatepush | 是否已下达 | bpchar | 1 |  | √ | '0' | 是否已下达 |
| 5 | fsrctypeid | 寻源流程 | int8 | 64 |  | √ | 0 | 流程配置 pds_flowconfig |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fscoretype | 评分方式 | bpchar | 1 |  | √ | ' ' | 评分方式,枚举: 1 :评委直接在系统打分 2 :评委手工评分后录入系统 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fopentype | 开标顺序 | bpchar | 1 |  | √ | ' ' | 开标顺序,枚举: 1 :同时开技术标和商务标 2 :先开评技术标，后开商务标 |
| 10 | fdatefrom | 考评期间从 | timestamp | 0 |  |  | null | 考评期间从 |
| 11 | fishidesupplier | 评分时是否隐藏专家姓名 | bpchar | 1 |  | √ | '0' | 评分时是否隐藏专家姓名 |
| 12 | fbiztypeid | 考评类型 | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 13 | fmanagetype | 管理方式 | bpchar | 1 |  | √ | ' ' | 管理方式,枚举: 1 :按项目 2 :按标段 3 :按标的 |
| 14 | fbillno | 考评单号 | varchar | 50 |  | √ | ' ' | 考评单号 |
| 15 | fbidname | 考评名称 | varchar | 300 |  | √ | ' ' | 考评名称 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fdateto | 考评期间至 | timestamp | 0 |  |  | null | 考评期间至 |
| 18 | ftemplateid | 模板 | int8 | 64 |  | √ | 0 | 组件模板配置 pds_tplconfig |
| 19 | fperiodid | 考评周期 | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 20 | fprojectid | 寻源项目 | int8 | 64 |  | √ | 0 | 招标项目F7 src_projectf7 |
| 21 | fischanged | 考评结果是否更新专家库 | bpchar | 1 |  | √ | '1' | 考评结果是否更新专家库 |
| 22 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 23 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 24 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 25 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 26 | fdescription | 考评描述 | varchar | 255 |  | √ | ' ' | 考评描述 |
| 27 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 28 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 29 | fsourcetypeid | 寻源方式 | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 30 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_evaluate_number |  | fbillno |
| 2 | pk_src_evaluate |  | fid |
