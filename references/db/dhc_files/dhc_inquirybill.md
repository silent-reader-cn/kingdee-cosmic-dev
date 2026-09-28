# 共享问询工单-dhc_inquirybill

## 共享问询工单-多语言表 t_dhc_inquirybill_l

- **表名称：** 共享问询工单-多语言表
- **表名：** t_dhc_inquirybill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fposition | 职位 | varchar | 80 |  | √ | ' ' | 职位 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_dhc_inquirybilll_fidlid |  | fid,flocaleid |
| 2 | pk_dhc_inquirybill_l |  | fpkid |

---

## 共享问询工单-主表 t_dhc_inquirybill

- **表名称：** 共享问询工单-主表
- **表名：** t_dhc_inquirybill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已完成 |
| 4 | fapplydate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 5 | fquestiondesc | 问题描述 | varchar | 255 |  | √ | ' ' | 问题描述 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fdept | 部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fquestionreply | 问题回复 | varchar | 255 |  | √ | ' ' | 问题回复 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fquestionsubtypeid | 问题细类 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fposition | fposition | varchar | 80 |  | √ | ' ' |  |
| 14 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 15 | fquestiontypeid | 问题类型 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 16 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fcompanyid | 申请人公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_dhc_inquirybill |  | fid |
| 2 | idx_dhc_inquirybill_fbno |  | fbillno |
