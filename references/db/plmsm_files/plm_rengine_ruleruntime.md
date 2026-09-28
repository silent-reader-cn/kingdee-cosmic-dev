# 运行时规则（规则引擎）-plm_rengine_ruleruntime

## 运行时规则（规则引擎）-多语言表 t_plm_egn_drlrule_l

- **表名称：** 运行时规则（规则引擎）-多语言表
- **表名：** t_plm_egn_drlrule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 4 | frulename | 规则名称 | varchar | 100 |  | √ | ' ' | 规则名称 |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_egn_drlrule_l |  | fpkid |
| 2 | idx_plm_drlrule_l |  | fid,flocaleid |

---

## 运行时规则（规则引擎）-主表 t_plm_egn_drlrule

- **表名称：** 运行时规则（规则引擎）-主表
- **表名：** t_plm_egn_drlrule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbizapp | 应用 | varchar | 50 |  | √ | ' ' | 应用 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fkbasekey | kbasekey | varchar | 200 |  | √ | ' ' | kbasekey |
| 6 | ftenantid | 租户id | varchar | 100 |  | √ | ' ' | 租户id |
| 7 | fruledesignid | 设计时规则 | int8 | 64 |  | √ | 0 | [规则设计（规则引擎） plm_rengine_ruledesign](../plmsm_files/plm_rengine_ruledesign.md) |
| 8 | fpackagename | packagename | varchar | 200 |  | √ | ' ' | packagename |
| 9 | frulecontent | 规则内容 | text | 0 |  |  | null | 规则内容 |
| 10 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 11 | fpolicyid | 所属策略 | int8 | 64 |  | √ | 0 | [规则设计（规则引擎） plm_rengine_ruledesign](../plmsm_files/plm_rengine_ruledesign.md) |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fscene | 场景 | varchar | 50 |  | √ | ' ' | 场景 |
| 15 | frulename | 规则名称 | varchar | 100 |  | √ | ' ' | 规则名称 |
| 16 | fruleorder | 优先级 | int4 | 32 |  | √ | 0 | 优先级 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_egn_drlrule |  | fid |
| 2 | idx_plm_drlrule |  | fruledesignid |
