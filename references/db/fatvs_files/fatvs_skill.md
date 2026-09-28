# 技能-fatvs_skill

## 技能-主表 t_fatvs_skill

- **表名称：** 技能-主表
- **表名：** t_fatvs_skill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | funlocktime | 解锁/锁定时间 | timestamp | 0 |  |  | null | 解锁/锁定时间 |
| 3 | fbelongapp | 所属应用 | varchar | 50 |  | √ | ' ' | 所属应用 |
| 4 | fclasspath | 获取运行数据实现类 | varchar | 255 |  | √ | ' ' | 获取运行数据实现类 |
| 5 | fskillvalue | 技能价值 | varchar | 255 |  | √ | ' ' | 技能价值 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | foffice | 所属办公室 | int8 | 64 |  | √ | 0 | 办公室 fatvs_office |
| 8 | funlocktype | 解锁类型 | varchar | 50 |  | √ | ' ' | 解锁类型,枚举: 0 :常规许可校验 1 :税务云专属许可校验 |
| 9 | fstatus | 数据状态 | varchar | 2 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fdistributestatus | 分配状态 | bpchar | 1 |  | √ | '0' | 分配状态 |
| 13 | fpicturefield | 技能图片 | varchar | 255 |  | √ | ' ' | 技能图片 |
| 14 | fformid | 技能运行分析页 | varchar | 50 |  | √ | ' ' | 技能运行分析页 |
| 15 | fname | 技能名称 | varchar | 50 |  | √ | ' ' | 技能名称 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | flaborcost | 每月人工成本 | numeric | 23 | 10 | √ | 0 | 每月人工成本 |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fdescription | 技能描述 | varchar | 255 |  | √ | ' ' | 技能描述 |
| 20 | fdistributetime | 分配日期 | timestamp | 0 |  |  | null | 分配日期 |
| 21 | funlockstatus | 是否解锁 | bpchar | 1 |  | √ | '0' | 是否解锁 |
| 22 | femployee | 分配数字员工 | int8 | 64 |  | √ | 0 | 形象库 fatvs_employee |
| 23 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 24 | flaborefficiency | 每月人工处理任务数 | int8 | 64 |  | √ | 0 | 每月人工处理任务数 |
| 25 | fnumber | 技能编码 | varchar | 50 |  | √ | ' ' | 技能编码 |
| 26 | fbelonglicensegroup | 所属许可分组 | varchar | 50 |  | √ | ' ' | 所属许可分组 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fatvs_skill_employee |  | femployee |
| 2 | pk_t_fatvs_skill |  | fid |
| 3 | idx_fatvs_skill_office |  | foffice |

---

## 技能-多语言表 t_fatvs_skill_l

- **表名称：** 技能-多语言表
- **表名：** t_fatvs_skill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 技能名称 | varchar | 50 |  | √ | ' ' | 技能名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 技能描述 | varchar | 255 |  | √ | ' ' | 技能描述 |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 6 | fskillvalue | 技能价值 | varchar | 255 |  | √ | ' ' | 技能价值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fatvs_skill_l |  | fid,flocaleid |
| 2 | pk_t_fatvs_skill_l |  | fpkid |

---

## 技能标签-多选基础资料表 t_fatvs_skill_relatedflag

- **表名称：** 技能标签-多选基础资料表
- **表名：** t_fatvs_skill_relatedflag

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 技能标签 fatvs_skillflag |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fatvs_skill_related_fid |  | fid |
| 2 | pk_t_fatvs_skill_relatedflag |  | fpkid |
