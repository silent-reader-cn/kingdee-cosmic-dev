# 技能-msmob_skill

## 所属技能族-多选基础资料表 t_msmob_skill_skillfamily

- **表名称：** 所属技能族-多选基础资料表
- **表名：** t_msmob_skill_skillfamily

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [技能族 msmob_skill_family](../msmob_files/msmob_skill_family.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msmob_skill_skillfamily_fk |  | fid |
| 2 | pk_t_msmob_skill_skillfamily |  | fpkid |

---

## 技能-多语言表 t_msmob_scan_skill_l

- **表名称：** 技能-多语言表
- **表名：** t_msmob_scan_skill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 技能名称 | varchar | 50 |  | √ | ' ' | 技能名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 技能说明 | varchar | 255 |  | √ | ' ' | 技能说明 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msmob_skills_l_0 |  | fid,flocaleid |
| 2 | pk_t_msmob_scan_skill_l |  | fpkid |

---

## 技能-主表 t_msmob_scan_skill

- **表名称：** 技能-主表
- **表名：** t_msmob_scan_skill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 技能名称 | varchar | 50 |  | √ | ' ' | 技能名称 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fdescription | 技能说明 | varchar | 255 |  | √ | ' ' | 技能说明 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fissystem | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 11 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 12 | fpluginclasspath | 实现插件类 | varchar | 255 |  | √ | ' ' | 实现插件类 |
| 13 | fnumber | 技能编码 | varchar | 50 |  | √ | ' ' | 技能编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msmob_scan_skill |  | fid |
| 2 | idx_msmob_skills_name |  | fnumber,fname |
