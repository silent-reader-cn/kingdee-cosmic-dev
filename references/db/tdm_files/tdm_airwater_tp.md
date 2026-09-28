# 大气水污染信息暂存关系-tdm_airwater_tp

## 大气水污染信息暂存关系-主表 t_tdm_airwater_tp

- **表名称：** 大气水污染信息暂存关系-主表
- **表名：** t_tdm_airwater_tp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | ftype | 污染物种类及其计算方法 | varchar | 200 |  | √ | ' ' | 污染物种类及其计算方法,枚举: first :一类水、二类水、大气污染物-监测计算法 second :一类水、二类水、大气污染物-产排污系数法 third :一类水、二类水、大气污染物-物料衡算法 fourth :PH值、色度、大肠菌群数、余氯量水污染物 five :禽畜养殖业、小型企业和第三产业-抽样测算法 six :施工排放扬尘-抽样测算法 |
| 11 | fmonth | 税款所属月份 | timestamp | 0 |  |  | null | 税款所属月份 |
| 12 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tdm_airwater_tp |  | fid |
| 2 | idx_tdm_airwater_tp |  | fnumber |

---

## 大气水污染信息暂存关系-多语言表 t_tdm_airwater_tp_l

- **表名称：** 大气水污染信息暂存关系-多语言表
- **表名：** t_tdm_airwater_tp_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_airwater_tp_l_0 |  | fid,flocaleid |
| 2 | pk_tdm_airwater_tp_l |  | fpkid |
