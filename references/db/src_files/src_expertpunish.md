# 专家处罚-src_expertpunish

## 专家处罚-主表 t_src_expertpunish

- **表名称：** 专家处罚-主表
- **表名：** t_src_expertpunish

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexpertid | 专家 | int8 | 64 |  | √ | 0 | 专家资料 src_expert |
| 3 | forgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fbilldate | 处罚时间 | timestamp | 0 |  |  | null | 处罚时间 |
| 5 | funauditdate | 反审核时间 | timestamp | 0 |  |  | null | 反审核时间 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fisselfhelp | 是否专家自助 | bpchar | 1 |  | √ | '0' | 是否专家自助 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | funauditorid | 反审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fbillno | 处罚编号 | varchar | 30 |  | √ | ' ' | 处罚编号 |
| 11 | fitemtypeid | 处罚类型 | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 12 | fbizorg | 处罚单位 | varchar | 255 |  | √ | ' ' | 处罚单位 |
| 13 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | funsubmitterid | 撤销人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | funsubmitdate | 撤销时间 | timestamp | 0 |  |  | null | 撤销时间 |
| 17 | fprojectid | 寻源项目 | int8 | 64 |  | √ | 0 | 招标项目F7 src_projectf7 |
| 18 | fgradeid | 对专家库的影响(考评等级) | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 19 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 20 | fsubmitterid | 提交人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 23 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 24 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 25 | fsubmitdate | 提交时间 | timestamp | 0 |  |  | null | 提交时间 |
| 26 | fitemname | 处罚名称 | varchar | 255 |  | √ | ' ' | 处罚名称 |
| 27 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_expertpunish |  | fid |
| 2 | idx_src_expertpunish_fexpertid |  | fexpertid |
| 3 | idx_src_expertpunish_fbillno |  | fbillno |
