# 拜访计划-occbo_visit

## 拜访计划-关联追踪表 t_occbo_visit_tc

- **表名称：** 拜访计划-关联追踪表
- **表名：** t_occbo_visit_tc

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
| 1 | pk_occbo_visit_tc |  | fid |
| 2 | idx_occbo_visit_tc_tbill |  | ftbillid |
| 3 | idx_occbo_visit_tc_tid |  | ftid |

---

## 关联子实体-子表 t_occbo_visit_lk

- **表名称：** 关联子实体-子表
- **表名：** t_occbo_visit_lk

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
| 1 | pk_occbo_visit_lk |  | fpkid |
| 2 | idx_occbo_visit_lk_fk |  | fid |

---

## 拜访记录-子表 t_occbo_visitentry

- **表名称：** 拜访记录-子表
- **表名：** t_occbo_visitentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fopstatus | 执行状态 | bpchar | 1 |  | √ | 'A' | 执行状态,枚举: A :未执行 B :已执行 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fbillentityid | 单据实体 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 5 | fbillnos | 单据编号 | varchar | 2000 |  | √ | ' ' | 单据编号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fvisitthingsid | 拜访事务 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occbo_visitentry_fid |  | fid |
| 2 | pk_occbo_visitentry |  | fentryid |

---

## 拜访计划-主表 t_occbo_visit

- **表名称：** 拜访计划-主表
- **表名：** t_occbo_visit

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcompleteinfo | 完成情况 | varchar | 255 |  | √ | ' ' | 完成情况 |
| 3 | fcheckouttime | 签退时间 | timestamp | 0 |  |  | null | 签退时间 |
| 4 | fsalerid | 业务员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fparentchannelid | 所属上级 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fprovinceid | 所属省区 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fsourcebillld | 来源单据 | int8 | 64 |  | √ | 0 | 来源单据 |
| 10 | fsourcetype | 来源单据类型 | bpchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 11 | fchannelid | 拜访渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 12 | fcheckintime | 签到时间 | timestamp | 0 |  |  | null | 签到时间 |
| 13 | fvisitstatus | 拜访状态 | bpchar | 1 |  | √ | 'A' | 拜访状态,枚举: A :计划 B :进行中 C :已完成 D :已取消 |
| 14 | fextravisitdate | 实际拜访日期 | timestamp | 0 |  |  | null | 实际拜访日期 |
| 15 | fcheckinaddress | 签到地址 | varchar | 255 |  | √ | ' ' | 签到地址 |
| 16 | fbillno | 拜访编号 | varchar | 80 |  | √ | ' ' | 拜访编号 |
| 17 | fplanvisitdate | 拜访日期 | timestamp | 0 |  |  | null | 拜访日期 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fpicture6 | 图片字段 | varchar | 500 |  | √ | ' ' | 图片字段 |
| 20 | fpicture5 | 图片字段 | varchar | 500 |  | √ | ' ' | 图片字段 |
| 21 | fsourceentryld | 来源分录 | int8 | 64 |  | √ | 0 | 来源分录 |
| 22 | fpicture4 | 图片字段 | varchar | 500 |  | √ | ' ' | 图片字段 |
| 23 | fcomment | 拜访内容 | varchar | 2000 |  | √ | ' ' | 拜访内容 |
| 24 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 25 | fpicture3 | 图片字段 | varchar | 500 |  | √ | ' ' | 图片字段 |
| 26 | fsummarize | 拜访总结 | varchar | 2000 |  | √ | ' ' | 拜访总结 |
| 27 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 28 | fpicture2 | 图片字段 | varchar | 500 |  | √ | ' ' | 图片字段 |
| 29 | fpicture1 | 图片字段 | varchar | 500 |  | √ | ' ' | 图片字段 |
| 30 | fregionid | 所属大区 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 31 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 32 | fdepartmentid | 所属部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 33 | fdistance | 距离差（米） | numeric | 23 | 10 | √ | 0 | 距离差（米） |
| 34 | fplanbegintime | 计划时间 | int4 | 32 |  | √ | 0 | 计划时间 |
| 35 | fsourcenumber | 来源单据编码 | varchar | 80 |  | √ | ' ' | 来源单据编码 |
| 36 | fchecktimerange | 拜访时长（小时） | numeric | 23 | 10 | √ | 0 | 拜访时长（小时） |
| 37 | fvisittypeid | 拜访类型 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 38 | flongitude | 签到经度 | numeric | 23 | 10 | √ | 0 | 签到经度 |
| 39 | fsourcesubentryld | 来源子分录 | int8 | 64 |  | √ | 0 | 来源子分录 |
| 40 | flatitude | 签到纬度 | numeric | 23 | 10 | √ | 0 | 签到纬度 |
| 41 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occbo_visit_billno |  | fbillno |
| 2 | pk_occbo_visit |  | fid |

---

## 拜访计划-反写记录表 t_occbo_visit_wb

- **表名称：** 拜访计划-反写记录表
- **表名：** t_occbo_visit_wb

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
| 1 | pk_occbo_visit_wb |  | fentryid |
| 2 | idx_occbo_visit_wb_fk |  | fid |
