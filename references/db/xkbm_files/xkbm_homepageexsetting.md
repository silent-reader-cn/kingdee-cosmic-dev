# 预算首页执行进度设置-xkbm_homepageexsetting

## 预算首页执行进度设置-主表 t_xkbm_homepageexsetting

- **表名称：** 预算首页执行进度设置-主表
- **表名：** t_xkbm_homepageexsetting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fxkbmbusinessservice | 预算业务服务 | int8 | 64 |  | √ | 0 | [预算业务服务 xkbm_businessservice](../xkbm_files/xkbm_businessservice.md) |
| 3 | fctrlrule | 预算控制规则 | int8 | 64 |  | √ | 0 | [预算控制规则 xkbm_ctrlrule](../xkbm_files/xkbm_ctrlrule.md) |
| 4 | fcurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 5 | fperiod | 期间 | varchar | 30 |  | √ | '1' | 期间,枚举: 1 :上期 2 :当期 |
| 6 | fbusinesstype | 预算业务类型 | int8 | 64 |  | √ | 0 | [预算业务类型 xkbm_businesstype](../xkbm_files/xkbm_businesstype.md) |
| 7 | fuserid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fitemdatatype | 项目数据类型 | int8 | 64 |  | √ | 0 | [项目数据类型 xkbm_rptitemdatatype](../fibd_files/xkbm_rptitemdatatype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_homepageexsetting |  | fid |
| 2 | idx_xkbm_homepage_ex_set |  | fuserid,fxkbmbusinessservice |

---

## 单据体-子表 t_xkbm_home_ex_entry

- **表名称：** 单据体-子表
- **表名：** t_xkbm_home_ex_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffiltername | 维度范围 | varchar | 2000 |  | √ | ' ' | 维度范围 |
| 3 | fdimeffectdesc | 过滤条件JSON | varchar | 2000 |  | √ | ' ' | 过滤条件JSON |
| 4 | fdimeffectname | 维度过滤 | varchar | 2000 |  | √ | ' ' | 维度过滤 |
| 5 | fisdimensionsum | 汇总 | bpchar | 1 |  | √ | '0' | 汇总 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | ffilterkey | 维度范围Sql | varchar | 2000 |  | √ | ' ' | 维度范围Sql |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fdimeffectkey | 维度过滤条件 | varchar | 2000 |  | √ | ' ' | 维度过滤条件 |
| 10 | fdimension | 报告维度 | int8 | 64 |  | √ | 0 | [维度 xkrpt_dimension](../xkrpt_files/xkrpt_dimension.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_home_ex_entry |  | fentryid |
| 2 | idx_xkbm_homepage_ex_en |  | fdimension |
