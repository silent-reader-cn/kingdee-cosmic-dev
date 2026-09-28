# 企业主要客户及项目情况-srm_cmtmain

## 企业主要客户及项目情况-主表 t_srm_compentcustomer

- **表名称：** 企业主要客户及项目情况-主表
- **表名：** t_srm_compentcustomer

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
| 1 | pk_t_srm_compentcustomer |  | fid |
| 2 | idx_srm_cptcustomer_parent |  | fparentid |

---

## 主要客户及项目情况-子表 t_srm_compcustomerentry

- **表名称：** 主要客户及项目情况-子表
- **表名：** t_srm_compcustomerentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprojectname | 项目名称及内容 | varchar | 255 |  | √ | ' ' | 项目名称及内容 |
| 3 | fname | 客户名称 | varchar | 255 |  | √ | ' ' | 客户名称 |
| 4 | faddress | 实施地点 | varchar | 255 |  | √ | ' ' | 实施地点 |
| 5 | ffield | 客户所属行业 | varchar | 255 |  | √ | ' ' | 客户所属行业 |
| 6 | fdateend | 项目结束时间 | timestamp | 0 |  |  | null | 项目结束时间 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fcontractamount | 合同金额 | numeric | 23 | 10 | √ | 0 | 合同金额 |
| 9 | fproduct | 主要应用到的产品 | varchar | 255 |  | √ | ' ' | 主要应用到的产品 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fdatabegain | 项目开始时间 | timestamp | 0 |  |  | null | 项目开始时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_srm_customerentry_fid |  | fid |
| 2 | pk_t_srm_compcustomerentry |  | fentryid |
