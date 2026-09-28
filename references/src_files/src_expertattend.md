# 专家考勤-src_expertattend

## 专家考勤-主表 t_src_expertattend

- **表名称：** 专家考勤-主表
- **表名：** t_src_expertattend

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
| 8 | fdatefrom | 评标开始时间 | timestamp | 0 |  |  | null | 评标开始时间 |
| 9 | funauditorid | 反审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fsigndatefrom | 签到开始时间 | timestamp | 0 |  |  | null | 签到开始时间 |
| 11 | fbillno | 考勤单号 | varchar | 30 |  | √ | ' ' | 考勤单号 |
| 12 | fitemtypeid | 考勤结果 | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 13 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fdateto | 评标结束时间 | timestamp | 0 |  |  | null | 评标结束时间 |
| 16 | funsubmitterid | 撤销人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | funsubmitdate | 撤销时间 | timestamp | 0 |  |  | null | 撤销时间 |
| 18 | fprojectid | 寻源项目 | int8 | 64 |  | √ | 0 | 招标项目F7 src_projectf7 |
| 19 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 20 | fsubmitterid | 提交人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | fsigndateto | 签到结束时间 | timestamp | 0 |  |  | null | 签到结束时间 |
| 23 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 24 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 25 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 26 | fsubmitdate | 提交时间 | timestamp | 0 |  |  | null | 提交时间 |
| 27 | fitemname | 事项名称 | varchar | 255 |  | √ | ' ' | 事项名称 |
| 28 | fnumber | 评标时长(小时) | numeric | 19 | 6 | √ | 0 | 评标时长(小时) |
| 29 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_expertattend_fbillno |  | fbillno |
| 2 | pk_src_expertattend |  | fid |
| 3 | idx_src_expertattend_fexpertid |  | fexpertid |

---

## 参标类型-多选基础资料表 t_src_bidtype

- **表名称：** 参标类型-多选基础资料表
- **表名：** t_src_bidtype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_src_bidtype_fid |  | fid |
| 2 | pk_src_bidtype |  | fpkid |
