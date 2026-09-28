# 周期性收支计划维护-fpm_cronplanmaintain

## 周期性收支计划维护-主表 t_fpm_cronplanmaintain

- **表名称：** 周期性收支计划维护-主表
- **表名：** t_fpm_cronplanmaintain

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ffirstexpectdate | 首次生成的期望日期 | timestamp | 0 |  |  | null | 首次生成的期望日期 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | 模板名称 | varchar | 100 |  | √ | ' ' | 模板名称 |
| 5 | fextra1 | 自定义字段1 | varchar | 255 |  | √ | ' ' | 自定义字段1 |
| 6 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | ffuturethreeexpectdate | 预计未来3期的期望日期 | varchar | 50 |  | √ | ' ' | 预计未来3期的期望日期 |
| 9 | fotherinfo | 其他信息 | varchar | 256 |  | √ | ' ' | 其他信息 |
| 10 | frecentrecordexpectdate | 最近一期生成记录的期望日期 | timestamp | 0 |  |  | null | 最近一期生成记录的期望日期 |
| 11 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 12 | fextra4 | 自定义字段4 | varchar | 255 |  | √ | ' ' | 自定义字段4 |
| 13 | fdepartmentid | 部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 14 | fextra5 | 自定义字段5 | varchar | 255 |  | √ | ' ' | 自定义字段5 |
| 15 | fextra2 | 自定义字段2 | varchar | 255 |  | √ | ' ' | 自定义字段2 |
| 16 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 17 | fextra3 | 自定义字段3 | varchar | 255 |  | √ | ' ' | 自定义字段3 |
| 18 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fexpiredate | 模板失效日期 | timestamp | 0 |  |  | null | 模板失效日期 |
| 20 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | finoutcycle | 收支周期 | varchar | 50 |  | √ | ' ' | 收支周期,枚举: Month :按月 Week :按周 Year :按年 |
| 22 | fbillno | 模板编码 | varchar | 50 |  | √ | ' ' | 模板编码 |
| 23 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | frepeatcycle | 重复周期 | int4 | 32 |  | √ | 0 | 重复周期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cronplanmaintain |  | fbillno |
| 2 | pk_t_fpm_cronplanmaintain |  | fid |

---

## 周期性收支计划维护-分表 t_fpm_cronplanmaintain_e

- **表名称：** 周期性收支计划维护-分表
- **表名：** t_fpm_cronplanmaintain_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffundorgid | 收付组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fremark | 备注 | varchar | 256 |  | √ | ' ' | 备注 |
| 4 | fcurrentplanamount | 本次计划金额 | numeric | 23 | 10 | √ | 0 | 本次计划金额 |
| 5 | fapplyorgid | 业务单元 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 7 | ffundpurposeid | 资金用途 | int8 | 64 |  | √ | 0 | [资金用途 cas_fundflowitem](../cas_files/cas_fundflowitem.md) |
| 8 | fcontractname | 合同名称 | varchar | 50 |  | √ | ' ' | 合同名称 |
| 9 | fbusinesstype | 业务类型 | varchar | 50 |  | √ | ' ' | 业务类型,枚举: InOutPlanApply :收支计划申报 |
| 10 | fexpectdate | 期望日期 | timestamp | 0 |  |  | null | 期望日期 |
| 11 | fexpectcashamount | 期望收付金额 | numeric | 23 | 10 | √ | 0 | 期望收付金额 |
| 12 | fopusername | 往来单位名称 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 13 | fcorebillremaincashamt | 核心单据剩余收付金额 | numeric | 23 | 10 | √ | 0 | 核心单据剩余收付金额 |
| 14 | fcontractno | 合同编号 | varchar | 50 |  | √ | ' ' | 合同编号 |
| 15 | ffeeprojectid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 16 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 17 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 18 | fapplyuserid | 申报人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fcurrentplandate | 本次计划日期 | timestamp | 0 |  |  | null | 本次计划日期 |
| 20 | finoutdirection | 收支方向 | varchar | 50 |  | √ | ' ' | 收支方向,枚举: In :流入 Out :流出 Other :其他 |
| 21 | fopusertype | 往来单位类型 | varchar | 50 |  | √ | ' ' | 往来单位类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :职员 bos_org :公司 cas_othercontactunit :其他往来单位 other :其他 |
| 22 | fcorebillsumamount | 核心单据业务总额 | numeric | 23 | 10 | √ | 0 | 核心单据业务总额 |
| 23 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cronplan_applyorg |  | ffundorgid |
| 2 | pk_t_fpm_cronplanmaintain_e |  | fid |
