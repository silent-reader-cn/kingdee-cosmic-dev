# 指标卡片-sbs_topiccard

## 指标卡片-多语言表 t_sbs_topiccard_l

- **表名称：** 指标卡片-多语言表
- **表名：** t_sbs_topiccard_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 卡片名称 | varchar | 512 |  | √ | ' ' | 卡片名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sbs_topiccard_l |  | fpkid |
| 2 | idx_sbs_topiccard_l_id |  | fid,flocaleid |

---

## 指标卡片-主表 t_sbs_topiccard

- **表名称：** 指标卡片-主表
- **表名：** t_sbs_topiccard

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | freleasetime | 发布/取消发布时间 | timestamp | 0 |  |  | null | 发布/取消发布时间 |
| 3 | fname | 卡片名称 | varchar | 512 |  | √ | ' ' | 卡片名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fgroupid | 卡片分组 | int8 | 64 |  | √ | 0 | [指标卡片分组 sbs_topiccardgroup](../sbs_files/sbs_topiccardgroup.md) |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 8 | freleasestatus | 发布状态 | bpchar | 1 |  | √ | ' ' | 发布状态,枚举: A :已发布 B :未发布 |
| 9 | findexid | 指标名称 | int8 | 64 |  | √ | 0 | 数智指标 didc_indexcatalogue |
| 10 | fcardconfig_tag | 卡片配置数据_详情 | text | 0 |  |  | '' | 卡片配置数据_详情 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fcardconfig | 卡片配置数据 | text | 0 |  |  | '' | 卡片配置数据 |
| 13 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fpreset | 系统预设 | bpchar | 1 |  | √ | ' ' | 系统预设 |
| 17 | fenable | 可用状态 | bpchar | 1 |  | √ | ' ' | 可用状态,枚举: 0 :禁用 1 :可用 |
| 18 | freleaser | 发布/取消发布人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fdisabler | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fnumber | 卡片编码 | varchar | 30 |  | √ | ' ' | 卡片编码 |
| 21 | findexfrom | 指标来源 | varchar | 100 |  | √ | ' ' | 指标来源,枚举: didc_indexcatalogue :数智指标 sbs_datametrics :供应链数据指标 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sbs_topiccard |  | fid |
| 2 | index_sbs_topiccard_id |  | fmasterid |

---

## 用户范围单据体-子表 t_sbs_topiccarduserentry

- **表名称：** 用户范围单据体-子表
- **表名：** t_sbs_topiccarduserentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftype | 类型 | varchar | 8 |  | √ | ' ' | 类型,枚举: user :用户 role :角色 |
| 3 | fuser | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | frole | 角色 | varchar | 100 |  | √ | ' ' | [通用角色 perm_role](../base_files/perm_role.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sbs_user_id |  | fid |
| 2 | pk_t_sbs_topiccarduserentry |  | fentryid |
