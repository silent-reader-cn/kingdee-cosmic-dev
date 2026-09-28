# 评价维度-pmm_commentmodule

## 评价维度-主表 t_mal_commentmodule

- **表名称：** 评价维度-主表
- **表名：** t_mal_commentmodule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 评价维度 | varchar | 80 |  | √ | ' ' | 评价维度 |
| 3 | fgroupid | 评价方式 | int8 | 64 |  | √ | 0 | [组件类型 pmm_moduletype](../pmm_files/pmm_moduletype.md) |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fispreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fnum | 数量 | bpchar | 1 |  | √ | ' ' | 数量,枚举: A :5星 |
| 9 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | flevel | 等级 | varchar | 50 |  | √ | ' ' | 等级,枚举: A :好评 B :中评 C :差评 |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fpicturenum | 附件数量 | bpchar | 1 |  | √ | ' ' | 附件数量,枚举: 1 :1张图片 2 :2张图片 3 :3张图片 4 :4张图片 5 :5张图片 |
| 14 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 16 | fscore | 打分制 | bpchar | 1 |  | √ | ' ' | 打分制,枚举: A :100分制 B :50分制 C :10分制 D :5分制 |
| 17 | fplaceholder | 提示语 | varchar | 255 |  | √ | ' ' | 提示语 |
| 18 | fdimensionparam | 维度配置 | varchar | 1734 |  | √ | ' ' | 维度配置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mal_commentmodule |  | fid |
| 2 | idx_mal_commodule_fnumber |  | fnumber |

---

## 标签-多选基础资料表 t_mal_commentmodulelabel

- **表名称：** 标签-多选基础资料表
- **表名：** t_mal_commentmodulelabel

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [评价标签 pmm_commentlabel](../pmm_files/pmm_commentlabel.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_commodulelab_fmasterid |  | fid |
| 2 | pk_t_mal_commentmodulelabel |  | fpkid |

---

## 评价维度-多语言表 t_mal_commentmodule_l

- **表名称：** 评价维度-多语言表
- **表名：** t_mal_commentmodule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 评价维度 | varchar | 80 |  | √ | ' ' | 评价维度 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fplaceholder | 提示语 | varchar | 255 |  | √ | ' ' | 提示语 |
| 6 | fdimensionparam | 维度配置 | varchar | 1734 |  | √ | ' ' | 维度配置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_commentmodule_l_fid |  | fid,flocaleid |
| 2 | pk_t_mal_commentmodule_l |  | fpkid |
