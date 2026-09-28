# 拜访计划-occbo_visit

## 拜访记录-子表 t_occbo_visitentry

- **表名称：** 拜访记录-子表
- **表名：** t_occbo_visitentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fopstatus | 执行状态 | bpchar | 1 |  | √ | 'A' | 执行状态,枚举: A :未执行 B :已执行 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fbillentityid | 单据实体 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 5 | fbillnos | 单据编号 | varchar | 2000 |  | √ | ' ' | 单据编号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fvisitthingsid | 拜访事务 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occbo_visitentry |  | fentryid |
| 2 | idx_occbo_visitentry_fid |  | fid |

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
| 4 | fsalerid | 业务员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fparentchannelid | 所属上级 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fprovinceid | 所属省区 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fchannelid | 拜访渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 10 | fcheckintime | 签到时间 | timestamp | 0 |  |  | null | 签到时间 |
| 11 | fvisitstatus | 拜访状态 | bpchar | 1 |  | √ | 'A' | 拜访状态,枚举: A :计划 B :进行中 C :已完成 D :已取消 |
| 12 | fextravisitdate | 实际拜访日期 | timestamp | 0 |  |  | null | 实际拜访日期 |
| 13 | fcheckinaddress | 签到地址 | varchar | 255 |  | √ | ' ' | 签到地址 |
| 14 | fbillno | 拜访编号 | varchar | 80 |  | √ | ' ' | 拜访编号 |
| 15 | fplanvisitdate | 拜访日期 | timestamp | 0 |  |  | null | 拜访日期 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fpicture6 | 图片字段 | varchar | 500 |  | √ | ' ' | 图片字段 |
| 18 | fpicture5 | 图片字段 | varchar | 500 |  | √ | ' ' | 图片字段 |
| 19 | fpicture4 | 图片字段 | varchar | 500 |  | √ | ' ' | 图片字段 |
| 20 | fcomment | 拜访内容 | varchar | 2000 |  | √ | ' ' | 拜访内容 |
| 21 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 22 | fpicture3 | 图片字段 | varchar | 500 |  | √ | ' ' | 图片字段 |
| 23 | fsummarize | 拜访总结 | varchar | 2000 |  | √ | ' ' | 拜访总结 |
| 24 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 25 | fpicture2 | 图片字段 | varchar | 500 |  | √ | ' ' | 图片字段 |
| 26 | fpicture1 | 图片字段 | varchar | 500 |  | √ | ' ' | 图片字段 |
| 27 | fregionid | 所属大区 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 28 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 29 | fdepartmentid | 所属部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 30 | fdistance | 距离差（米） | numeric | 23 | 10 | √ | 0 | 距离差（米） |
| 31 | fplanbegintime | 计划时间 | int4 | 32 |  | √ | 0 | 计划时间 |
| 32 | fchecktimerange | 拜访时长（小时） | numeric | 23 | 10 | √ | 0 | 拜访时长（小时） |
| 33 | fvisittypeid | 拜访类型 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 34 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occbo_visit_billno |  | fbillno |
| 2 | pk_occbo_visit |  | fid |
