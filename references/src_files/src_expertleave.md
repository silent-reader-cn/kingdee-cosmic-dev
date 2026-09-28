# 专家请假-src_expertleave

## 专家请假-主表 t_src_expertleave

- **表名称：** 专家请假-主表
- **表名：** t_src_expertleave

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexpertid | 专家 | int8 | 64 |  | √ | 0 | 专家资料 src_expert |
| 3 | forgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | funauditdate | 反审核时间 | timestamp | 0 |  |  | null | 反审核时间 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fisselfhelp | 是否专家自助 | bpchar | 1 |  | √ | '0' | 是否专家自助 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fdatefrom | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 9 | funauditorid | 反审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fbillno | 请假单号 | varchar | 30 |  | √ | ' ' | 请假单号 |
| 11 | fitemtypeid | 请假类型 | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 12 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 13 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fdateto | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 15 | funsubmitterid | 撤销人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | funsubmitdate | 撤销时间 | timestamp | 0 |  |  | null | 撤销时间 |
| 17 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fsubmitterid | 提交人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 22 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 23 | fsubmitdate | 提交时间 | timestamp | 0 |  |  | null | 提交时间 |
| 24 | fitemname | 请假事由 | varchar | 255 |  | √ | ' ' | 请假事由 |
| 25 | fnumber | 请假天数 | numeric | 19 | 6 | √ | 0 | 请假天数 |
| 26 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_expertleave_fexpertid |  | fexpertid |
| 2 | idx_src_expertleave_fbillno |  | fbillno |
| 3 | pk_src_expertleave |  | fid |
