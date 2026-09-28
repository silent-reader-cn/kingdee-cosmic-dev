# 技能预警详情-fatvs_warndetail

## 技能预警详情-多语言表 t_fatvs_warndetail_l

- **表名称：** 技能预警详情-多语言表
- **表名：** t_fatvs_warndetail_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | ftitlecontent | 标题内容 | varchar | 255 |  |  | ' ' | 标题内容 |
| 4 | fcontentvalue | 内容 | varchar | 1024 |  |  | ' ' | 内容 |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fatvs_warndetail_l |  | fid,flocaleid |
| 2 | pk_t_fatvs_warndetail_l |  | fpkid |

---

## 预警用户组-多选基础资料表 t_fatvs_warnusers

- **表名称：** 预警用户组-多选基础资料表
- **表名：** t_fatvs_warnusers

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [预警用户组 fatvs_warnusergroup](../fatvs_files/fatvs_warnusergroup.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fatvs_warnusers_fk |  | fid |
| 2 | pk_fatvs_warnusers |  | fpkid |

---

## 技能预警详情-主表 t_fatvs_warndetail

- **表名称：** 技能预警详情-主表
- **表名：** t_fatvs_warndetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fmaxvalue | 指标最大值 | varchar | 50 |  | √ | ' ' | 指标最大值 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 2 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fminvalue | 指标最小值 | varchar | 50 |  | √ | ' ' | 指标最小值 |
| 9 | falarmvalue | 警戒值 | varchar | 50 |  | √ | ' ' | 警戒值 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | femployee | 关联员工 | int8 | 64 |  | √ | 0 | [形象库 fatvs_employee](../fatvs_files/fatvs_employee.md) |
| 13 | ftitlecontent | 标题内容 | varchar | 255 |  | √ | ' ' | 标题内容 |
| 14 | findextype | 指标类型 | varchar | 50 |  | √ | ' ' | 指标类型,枚举: 0 :数字 1 :百分比 2 :文本 |
| 15 | fcomparestatus | 比较状态 | varchar | 50 |  | √ | ' ' | 比较状态,枚举: 0 :大于 1 :小于 2 :大于等于 3 :小于等于 |
| 16 | fenable | 启用状态 | bpchar | 1 |  | √ | '1' | 启用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fposition | 关联职位 | int8 | 64 |  | √ | 0 | [虚拟职位 fatvs_position](../fatvs_files/fatvs_position.md) |
| 18 | fcontentvalue | 内容 | varchar | 1024 |  | √ | ' ' | 内容 |
| 19 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 20 | fskillindex | 预警指标 | int8 | 64 |  | √ | 0 | [技能指标 fatvs_skill_index](../fatvs_files/fatvs_skill_index.md) |
| 21 | fskill | 预警技能 | int8 | 64 |  | √ | 0 | [技能 fatvs_skill](../fatvs_files/fatvs_skill.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fatvs_warndetail_sid |  | fskillindex |
| 2 | pk_t_fatvs_warndetail |  | fid |
| 3 | idx_fatvs_warndetail_nu |  | fnumber |
| 4 | idx_fatvs_warndetail_sk |  | fskill |
