# 补充工作单-pom_mrosws

## 关联子实体-子表 t_pom_mrosws_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pom_mrosws_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pom_mrosws_lk_fk |  | fid |
| 2 | pk_pom_mrosws_lk |  | fpkid |

---

## 补充工作单-关联追踪表 t_pom_mrosws_tc

- **表名称：** 补充工作单-关联追踪表
- **表名：** t_pom_mrosws_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  |  | null |  |
| 3 | fttableid | fttableid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | ftid | ftid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pom_mrosws_tc_tid |  | ftid |
| 2 | idx_pom_mrosws_tc_tbill |  | ftbillid |
| 3 | pk_pom_mrosws_tc |  | fid |

---

## 关联子实体-子表 t_pom_mroswsentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pom_mroswsentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pom_mroswsentry_lk |  | fpkid |
| 2 | idx_pom_mroswsentry_lk_fk |  | fentryid |

---

## 补充工作单-主表 t_pom_mrosws

- **表名称：** 补充工作单-主表
- **表名：** t_pom_mrosws

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fzone | 功能位置 | int8 | 64 |  | √ | 0 | 功能位置 mpdm_functionlocation |
| 3 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fattachmentcount | 附件数 | int8 | 64 |  | √ | 0 | 附件数 |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fcarduser | 出卡者 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fmaintrade | 主行业 | int8 | 64 |  | √ | 0 | 树形基础资料模板 mpdm_professiona |
| 9 | fworkcard | 工卡 | int8 | 64 |  | √ | 0 | 工卡 mpdm_mrocardroute |
| 10 | fsorderno | 来源检修工单号 | varchar | 50 |  | √ | ' ' | 来源检修工单号 |
| 11 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 12 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 13 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fcustomer | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 15 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | fsrcbillid | 来源检修工单id | int8 | 64 |  | √ | 0 | 来源检修工单id |
| 18 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 19 | fdatefield | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 20 | fworkhourunit | 工时单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 21 | fprintformat | 打印格式 | varchar | 50 |  | √ | ' ' | 打印格式,枚举: A :CWS B :DIC |
| 22 | fsrcbillentryid | 来源检修工单分录id | int8 | 64 |  | √ | 0 | 来源检修工单分录id |
| 23 | fplanhours | 计划消耗工时 | numeric | 23 | 10 | √ | 0 | 计划消耗工时 |
| 24 | fprintcount | 打印次数 | int8 | 64 |  | √ | 0 | 打印次数 |
| 25 | farea | 工作区域 | int8 | 64 |  | √ | 0 | 工作区域 mpdm_area |
| 26 | fmaterielmtc | 检修设备注册号 | int8 | 64 |  | √ | 0 | 物料检修信息 mpdm_materialmtcinfo |
| 27 | fproject | 项目号 | int8 | 64 |  | √ | 0 | 项目 pmpd_project |
| 28 | fworkstage | 工作类别 | int8 | 64 |  | √ | 0 | 工作类别 mpdm_workcategories |
| 29 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 30 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pom_mrosws_fbillno |  | fbillno |
| 2 | pk_im_pom_mrosws |  | fid |
| 3 | idx_pom_mrosws_forgid |  | forgid |

---

## 工作内容-子表 t_pom_mroswsentry

- **表名称：** 工作内容-子表
- **表名：** t_pom_mroswsentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprogroup | 工序组 | int8 | 64 |  | √ | 0 | 工序组(废弃) mpdm_progroup |
| 3 | fentrymodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fmanualversion | 版本号 | varchar | 50 |  | √ | ' ' | 版本号 |
| 5 | fentrycreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 6 | fworkhours | 工时 | numeric | 23 | 10 | √ | 0 | 工时 |
| 7 | fentrystatus | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: A :暂存 B :提交 C :审核 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fhelpmanual | fhelpmanual | varchar | 50 |  | √ | ' ' |  |
| 10 | fworkdesc | 工作描述 | varchar | 512 |  | √ | ' ' | 工作描述 |
| 11 | fhelphours | fhelphours | numeric | 23 | 10 | √ | 0 |  |
| 12 | fisexistorder | 是否已生成工单 | bpchar | 1 |  | √ | '0' | 是否已生成工单 |
| 13 | fentryauditor | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | frefmanual | 参考手册 | varchar | 50 |  | √ | ' ' | 参考手册,枚举: AMM :AMM WDM :WDM SRM :SRM SWPM :SWPM IPC :IPC CMM :CMM BULLETIN :BULLETIN OTHERS :OTHERS |
| 15 | fmanualcode | 文件编码 | varchar | 50 |  | √ | ' ' | 文件编码 |
| 16 | fmodifierfield | fmodifierfield | int8 | 64 |  | √ | 0 |  |
| 17 | forderno | 补充检修工单号 | varchar | 50 |  | √ | ' ' | 补充检修工单号 |
| 18 | fentrycreator | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fenworkhourunit | 工时单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 20 | fishelpmanual | 协助填写手册 | bpchar | 1 |  | √ | '0' | 协助填写手册 |
| 21 | fmodifydatefield | fmodifydatefield | timestamp | 0 |  |  | null |  |
| 22 | fhelpuser | 协助者 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 23 | frecheck | 复检 | bpchar | 1 |  | √ | '0' | 复检 |
| 24 | fdoctype | 文件类型 | int8 | 64 |  | √ | 0 | 文件类型 mpdm_doctype |
| 25 | fentryauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 26 | fprofessiona | 执行行业 | int8 | 64 |  | √ | 0 | 树形基础资料模板 mpdm_professiona |
| 27 | fishelphours | 协助填写预估工时 | bpchar | 1 |  | √ | '0' | 协助填写预估工时 |
| 28 | fishelp | 请求协助 | bpchar | 1 |  | √ | '0' | 请求协助 |
| 29 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 30 | fentrymodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pom_mroswsentry |  | fentryid |
| 2 | idx_pom_mroswsentry_fid |  | fid |

---

## 附件-附件表 t_pom_mroswsattachment

- **表名称：** 附件-附件表
- **表名：** t_pom_mroswsattachment

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
| 1 | idx_pom_swsattachment_fentryid |  | fentryid |
| 2 | pk_pom_mroswsattachment |  | fpkid |

---

## 补充工作单-反写记录表 t_pom_mrosws_wb

- **表名称：** 补充工作单-反写记录表
- **表名：** t_pom_mrosws_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 50 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 |  | null |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pom_mrosws_wb |  | fentryid |
| 2 | idx_pom_mrosws_wb_fk |  | fid |
