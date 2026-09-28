# 人员周计划-occbo_weeklyplan

## 单据体-子表 t_occbo_weeklyplan_entry

- **表名称：** 单据体-子表
- **表名：** t_occbo_weeklyplan_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fwhatday | 周几 | bpchar | 1 |  | √ | '0' | 周几,枚举: 1 :周一 2 :周二 3 :周三 4 :周四 5 :周五 6 :周六 0 :周日 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fitemclassid | 商品分类 | int8 | 64 |  | √ | 0 | [商品分类 mdr_item_class](../gmc_files/mdr_item_class.md) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fchannelid | 客户 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 7 | fiteminfoid | 产品 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fentrydate | 计划日期 | timestamp | 0 |  |  | null | 计划日期 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fkpiid | 任务 | int8 | 64 |  | √ | 0 | [KPI occbo_kpi_base](../occbo_files/occbo_kpi_base.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occbo_weeklyplan_entry |  | fentryid |
| 2 | idx_occbo_wplan_entry_fid |  | fid,fentrydate |

---

## 人员周计划-主表 t_occbo_weeklyplan

- **表名称：** 人员周计划-主表
- **表名：** t_occbo_weeklyplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 计划说明 | varchar | 255 |  |  | null | 计划说明 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fbegindate | 计划日期范围.开始 | timestamp | 0 |  |  | null | 计划日期范围.开始 |
| 7 | fplanname | 计划名称 | varchar | 80 |  | √ | ' ' | 计划名称 |
| 8 | fuserid | 计划人员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fweekordinal | 周数 | numeric | 23 | 10 | √ | 0 | 周数 |
| 10 | fregionid | 所属大区 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 12 | fdepartmentid | 所属部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fenddate | 计划日期范围.结束 | timestamp | 0 |  |  | null | 计划日期范围.结束 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fprovinceid | 所属省区 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 17 | fplandate | 计划日期 | timestamp | 0 |  |  | null | 计划日期 |
| 18 | fbillno | 计划编号 | varchar | 30 |  | √ | ' ' | 计划编号 |
| 19 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occbo_weeklyplan |  | fid |
| 2 | idx_occbo_weeklyplan_billno |  | fbillno |
