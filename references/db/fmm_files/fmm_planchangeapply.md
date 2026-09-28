# 主计划变更申请单-fmm_planchangeapply

## 主计划变更申请单-主表 t_fmm_planchangeapply

- **表名称：** 主计划变更申请单-主表
- **表名：** t_fmm_planchangeapply

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 2000 |  | √ | ' ' | 备注 |
| 3 | fapprovedate | fapprovedate | varchar | 2000 |  | √ | ' ' |  |
| 4 | fpassdate | fpassdate | timestamp | 0 |  |  | null |  |
| 5 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fapplydate | fapplydate | timestamp | 0 |  |  | null |  |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | forgid | 项目组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fworkscope | 工作内容 | int8 | 64 |  | √ | 0 | [工作内容 mpdm_workscopeins](../mpdm_files/mpdm_workscopeins.md) |
| 11 | fapplyuser | fapplyuser | int8 | 64 |  | √ | 0 |  |
| 12 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 13 | freason | 变更原因 | varchar | 2000 |  | √ | ' ' | 变更原因 |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fapproveuser | fapproveuser | int8 | 64 |  | √ | 0 |  |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fplantype | 项目计划类型 | int8 | 64 |  | √ | 0 | [项目计划类型 fmm_plantype](../fmm_files/fmm_plantype.md) |
| 18 | fproject | 项目号 | int8 | 64 |  | √ | 0 | [项目 pmpd_project](../fmm_files/pmpd_project.md) |
| 19 | fcontent | 变更内容 | varchar | 2000 |  | √ | ' ' | 变更内容 |
| 20 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 21 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fmm_planchangeapply_fno |  | fbillno |
| 2 | pk_fmm_planchangeapply |  | fid |
