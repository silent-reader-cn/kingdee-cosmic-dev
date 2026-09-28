# 专家业绩-src_expertwork

## 专家业绩-主表 t_src_expertwork

- **表名称：** 专家业绩-主表
- **表名：** t_src_expertwork

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
| 10 | fbillno | 业绩编号 | varchar | 30 |  | √ | ' ' | 业绩编号 |
| 11 | fitemtypeid | 业绩类型 | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 12 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 13 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fdateto | 评标结束时间 | timestamp | 0 |  |  | null | 评标结束时间 |
| 15 | funsubmitterid | 撤销人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | funsubmitdate | 撤销时间 | timestamp | 0 |  |  | null | 撤销时间 |
| 17 | fprojectid | 寻源项目 | int8 | 64 |  | √ | 0 | 招标项目F7 src_projectf7 |
| 18 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 19 | fsubmitterid | 提交人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 22 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 23 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 24 | fsubmitdate | 提交时间 | timestamp | 0 |  |  | null | 提交时间 |
| 25 | fitemname | 业绩名称 | varchar | 255 |  | √ | ' ' | 业绩名称 |
| 26 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_expertwork |  | fid |
| 2 | idx_src_expertwork_fbillno |  | fbillno |
| 3 | idx_src_expertwork_fexpertid |  | fexpertid |

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
