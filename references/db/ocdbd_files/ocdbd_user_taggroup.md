# 标签分组-ocdbd_user_taggroup

## 标签分组-主表 t_ocdbd_user_taggroup

- **表名称：** 标签分组-主表
- **表名：** t_ocdbd_user_taggroup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | '0' | 是否叶子 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 6 | fparentid | 上级 | int8 | 64 |  | √ | 0 | [标签分组 ocdbd_user_taggroup](../ocdbd_files/ocdbd_user_taggroup.md) |
| 7 | ffullname | 长名称 | varchar | 1000 |  | √ | ' ' | 长名称 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fcolorid | 标签颜色 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 10 | flongnumber | 长编码 | varchar | 1000 |  | √ | ' ' | 长编码 |
| 11 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fsrctypeid | 来源类型 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 13 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 14 | fispreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 15 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | fdisabletime | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 17 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | flevel | 级次 | int4 | 32 |  | √ | 0 | 级次 |
| 19 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 20 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 22 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 23 | fsrcuid | 来源唯一标识 | varchar | 80 |  | √ | ' ' | 来源唯一标识 |
| 24 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_user_taggroup |  | fid |
| 2 | idx_ocdbd_usertaggroup_num |  | fnumber |

---

## 标签分组-多语言表 t_ocdbd_user_taggroup_l

- **表名称：** 标签分组-多语言表
- **表名：** t_ocdbd_user_taggroup_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | ffullname | 长名称 | varchar | 1000 |  | √ | ' ' | 长名称 |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_user_taggroup_l |  | fpkid |
| 2 | idx_ocdbd_usertaggl_fidlid |  | fid,flocaleid |
